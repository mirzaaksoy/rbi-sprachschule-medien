#!/usr/bin/env python3
"""RBI Sprachschule – Grafik- und Reel-Renderer.
Aufruf: python3 tools/render.py spec.json
spec.json = Liste von Objekten:
  {"datei": "2026-12/rbi-22-thema", "stil": "werbung"|"lernen", "html": "<div class='main'>...</div>"}
  {"datei": "2026-12/rbi-23-thema", "stil": "reel", "folien": ["<div class='r'>...</div>", ...], "audio": "memos/23.m4a" (optional)}
Erzeugt .jpg (1080x1350) bzw. .mp4 (1080x1920) + -cover.jpg. Benötigt playwright + google-chrome + ffmpeg + Pillow.
Klassen siehe CSS unten und die bestehenden Posts als Vorbild (git log / 2026-11).
"""
import asyncio, json, sys, subprocess, pathlib, tempfile, shutil
from playwright.async_api import async_playwright
from PIL import Image
BASE = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#F6F1E9;color:#12302F;position:relative;overflow:hidden}
.band{position:absolute;left:0;right:0;top:0;height:14px;background:#1E7F7A}
.brand{position:absolute;top:70px;left:80px;font-size:26px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#1E7F7A}
.brand span{color:#12302F;opacity:.55;font-weight:500}
.tag{display:inline-block;background:#E8A33D;color:#12302F;font-weight:700;font-size:28px;padding:12px 24px;border-radius:999px}
.tag.red{background:#C8553D;color:#fff}
.main{position:absolute;left:80px;right:80px;top:200px}
h1{font-family:'Inter Display','Inter',sans-serif;font-size:110px;line-height:1.0;font-weight:800;letter-spacing:-.03em;margin-top:44px}
h1 em{font-style:normal;color:#1E7F7A}
.sub{font-size:38px;line-height:1.35;margin-top:36px;max-width:880px;opacity:.85}
.chips{display:flex;flex-wrap:wrap;gap:16px;margin-top:44px}
.chip{border:3px solid #12302F;border-radius:18px;padding:14px 24px;font-size:32px;font-weight:700}
.chip.on{background:#12302F;color:#F6F1E9}
.price{display:flex;gap:20px;margin-top:44px}
.pbox{flex:1;background:#fff;border-radius:24px;padding:28px 30px;box-shadow:0 2px 0 #12302F14}
.pbox small{display:block;font-size:26px;opacity:.65;font-weight:600}
.pbox b{display:block;font-size:64px;font-weight:800;color:#1E7F7A;margin-top:6px;letter-spacing:-.02em}
.list{margin-top:40px;font-size:36px;line-height:1.3}
.list div{padding:16px 0;border-bottom:2px solid #12302F1F;display:flex;justify-content:space-between;gap:20px}
.list div b{font-weight:800}
.foot{position:absolute;left:0;right:0;bottom:0;height:170px;background:#12302F;color:#F6F1E9;display:flex;align-items:center;justify-content:space-between;padding:0 80px}
.foot b{font-size:38px}
.foot small{display:block;font-size:25px;opacity:.7;margin-top:6px}
.cta{background:#E8A33D;color:#12302F;font-weight:800;font-size:30px;padding:22px 32px;border-radius:16px;white-space:nowrap}
.deco{position:absolute;right:-160px;top:420px;width:520px;height:520px;border-radius:50%;border:60px solid #1E7F7A;opacity:.12}
.big{font-family:'Inter Display','Inter',sans-serif;font-size:220px;font-weight:800;color:#1E7F7A;letter-spacing:-.04em;line-height:1}
"""
REEL_CSS = """
body{width:1080px;height:1920px}
.r{position:absolute;left:90px;right:90px;top:50%;transform:translateY(-50%)}
.r h1{font-size:130px}
.ex{background:#fff;border-radius:28px;padding:44px 48px;margin-top:40px;font-size:50px;line-height:1.3}
.ex b{color:#1E7F7A}
.ex .m{display:block;font-size:36px;opacity:.65;margin-top:14px}
.num{font-size:40px;font-weight:800;color:#E8A33D;letter-spacing:.06em}
.brand{top:120px;left:90px}
.foot{height:220px}
"""
LEARN_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:'Inter',sans-serif;background:#12302F;color:#F6F1E9;position:relative;overflow:hidden}
.band{position:absolute;left:0;right:0;top:0;height:14px;background:#E8A33D}
.brand{position:absolute;top:70px;left:80px;font-size:26px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#7FC8C3}
.brand span{color:#F6F1E9;opacity:.6;font-weight:500}
.tag{display:inline-block;background:#E8A33D;color:#12302F;font-weight:800;font-size:28px;padding:12px 24px;border-radius:999px}
.main{position:absolute;left:80px;right:80px;top:190px}
h1{font-size:96px;line-height:1.02;font-weight:800;letter-spacing:-.03em;margin-top:36px}
h1 em{font-style:normal;color:#7FC8C3}
.box{background:#1E3F3E;border-radius:26px;padding:26px 36px;margin-top:22px;font-size:38px;line-height:1.3}
.box b{color:#E8A33D}
.box small{display:block;font-size:28px;opacity:.7;margin-top:8px}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;margin-top:36px}
.col{background:#1E3F3E;border-radius:24px;padding:32px 28px}
.col .a{font-size:80px;font-weight:800;color:#E8A33D}
.col .e{font-size:36px;font-weight:700;margin:12px 0 22px;line-height:1.35;white-space:nowrap}
.col .w{font-size:31px;opacity:.85;line-height:1.55}
.no{color:#F08A6E}.ok{color:#7FC8C3}
.foot{position:absolute;left:0;right:0;bottom:0;height:150px;background:#1E7F7A;display:flex;align-items:center;justify-content:space-between;padding:0 80px}
.foot b{font-size:34px}.foot small{display:block;font-size:24px;opacity:.85;margin-top:4px}
.save{background:#F6F1E9;color:#12302F;font-weight:800;font-size:28px;padding:18px 26px;border-radius:14px}
"""
BRAND_W = "<div class='band'></div><div class='deco'></div><div class='brand'>RBI Sprachschule <span>· Düsseldorf · @rbi_sprachschule</span></div>"
LEARN_FOOT = "<div class='foot'><div><b>Deutsch lernen in Düsseldorf</b><small>@rbi_sprachschule · Intensivkurse A1–C1</small></div><div class='save'>📌 Speichern</div></div>"
def werbung(body): return f"<html><head><meta charset='utf-8'><style>{BASE}body{{width:1080px;height:1350px}}</style></head><body>{BRAND_W}{body}</body></html>"
def lernen(body): return f"<html><head><meta charset='utf-8'><style>{LEARN_CSS}</style></head><body><div class='band'></div><div class='brand'>RBI Sprachschule <span>· Deutsch-Tipp</span></div>{body}{LEARN_FOOT}</body></html>"
def folie(body, dark=False):
    extra = "body{background:#12302F;color:#F6F1E9}.ex{background:#1E3F3E;color:#F6F1E9}.brand{color:#7FC8C3}.brand span{color:#F6F1E9}h1 em{color:#7FC8C3}.foot{background:#1E7F7A}" if dark else ""
    return f"<html><head><meta charset='utf-8'><style>{BASE}{REEL_CSS}{extra}</style></head><body>{BRAND_W}{body}</body></html>"
def dauer(p):
    r=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True)
    return float(r.stdout.strip())
def video(frames, out, audio=None, fade=0.5):
    n=len(frames); dur=3.0
    if audio: dur=max(2.0,(dauer(audio)+0.8+fade*(n-1))/n)
    inp=[]
    for f in frames: inp+=["-loop","1","-t",f"{dur:.2f}","-i",f]
    filt=[];prev="[0:v]";off=dur-fade
    for i in range(1,n):
        filt.append(f"{prev}[{i}:v]xfade=transition=fade:duration={fade}:offset={off:.2f}[v{i}]");prev=f"[v{i}]";off+=dur-fade
    cmd=["ffmpeg","-y","-loglevel","error",*inp]
    if audio: cmd+=["-i",audio]
    cmd+=["-filter_complex",";".join(filt) if filt else "[0:v]null[v0]","-map",prev if filt else "[v0]"]
    if audio: cmd+=["-map",f"{n}:a","-af","loudnorm=I=-16:TP=-1.5,apad","-c:a","aac","-b:a","160k","-shortest"]
    cmd+=["-r","30","-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-movflags","+faststart",out]
    subprocess.run(cmd,check=True)
async def main(spec):
    tmp=pathlib.Path(tempfile.mkdtemp())
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=shutil.which("google-chrome") or "/usr/bin/google-chrome")
        for it in spec:
            out=pathlib.Path(it["datei"]); out.parent.mkdir(parents=True,exist_ok=True)
            if it["stil"] in ("werbung","lernen"):
                pg=await b.new_page(viewport={"width":1080,"height":1350})
                await pg.set_content((werbung if it["stil"]=="werbung" else lernen)(it["html"])); await pg.wait_for_timeout(200)
                png=tmp/(out.name+".png"); await pg.screenshot(path=str(png)); await pg.close()
                Image.open(png).convert("RGB").save(str(out)+".jpg","JPEG",quality=92)
            else:
                pg=await b.new_page(viewport={"width":1080,"height":1920}); frames=[]
                for i,h in enumerate(it["folien"]):
                    await pg.set_content(folie(h, dark=(i==len(it["folien"])-1))); await pg.wait_for_timeout(200)
                    f=tmp/f"{out.name}_{i}.png"; await pg.screenshot(path=str(f)); frames.append(str(f))
                await pg.close()
                Image.open(frames[0]).convert("RGB").save(str(out)+"-cover.jpg","JPEG",quality=92)
                video(frames,str(out)+".mp4",it.get("audio"))
            print("fertig:",out)
        await b.close()
if __name__=="__main__":
    asyncio.run(main(json.load(open(sys.argv[1],encoding="utf-8"))))
