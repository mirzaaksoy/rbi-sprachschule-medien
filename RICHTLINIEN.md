# Redaktionsrichtlinien – RBI Sprachschule (Instagram & Facebook)

Verbindlich für jeden automatischen Lauf. Bei Zweifel: Thema NICHT verwenden.

## Absender und Ton
- Name nach außen immer: **RBI Sprachschule** (Instagram @rbi_sprachschule, Website rbi-duesseldorf.de, Düsseldorf, nahe Hauptbahnhof).
- Anrede immer **„Sie“**. Freundlich, klar, motivierend, nicht übertrieben werblich. Deutsch; einfache Sätze, damit auch Lernende ab B1 folgen können.
- Emojis sparsam (2–6 pro Text). 5–9 Hashtags am Ende, immer `#rbisprachschule`.
- Instagram-Texte enden mit „Link in Bio“; Facebook-Texte nennen stattdessen „rbi-duesseldorf.de“.

## Leitbild pro Woche
- **Grundregel: Es gibt IMMER mehr Lern-Posts als Werbung** – in JEDER Kalenderwoche (Mo–So) mindestens 2 Deutsch-Tipps und höchstens 1 Werbepost. Keine Ausnahmen, auch nicht bei Fristen: Dann wird der Werbepost innerhalb der Woche verschoben, nicht zusätzlich eingeplant.
- Standard: **Montag: Deutsch-Tipp** · **Mittwoch: Werbung** · **Freitag: Deutsch-Tipp** (jeweils 10:58 Uhr). Der Werbetag darf innerhalb der Woche wechseln, wenn eine Frist es verlangt.
- Fristen beachten: Werbung für eine Anmeldefrist spätestens 3 Tage vor Fristende einplanen.
- Etwa jeder zweite Freitags-Tipp ist ein **Reel** (Folien-Video, 4–5 Folien), damit Sena (Lehrerin) eine Sprachaufnahme machen kann.

## Absolute Tabus (niemals)
- Keine christlichen oder anderen religiösen Feste und Bräuche: Weihnachten, Advent, Ostern, Karneval/Fasching, Halloween, Sankt Martin, Nikolaus usw. – auch nicht als Wortschatz.
- Keine Silvester-/Neujahrsfeiern, kein „Guten Rutsch“, kein „Frohes neues Jahr“. (Erlaubt: das neue Jahr als bloße Zeitangabe, z. B. „Kursstart im Januar“, „Neues Jahr, neues Deutsch“.)
- Kein Alkohol, auch nicht in Redewendungen (z. B. NICHT „Das ist nicht mein Bier“), kein Schweinefleisch, kein Glücksspiel, keine Dating-/Flirt-Themen, keine freizügigen Inhalte.
- Keine Politik, keine Religion allgemein, keine Witze über Herkunft oder Nationalitäten.
- Keine erfundenen Teilnehmerstimmen, Bewertungen oder Erfolgsquoten.
- Nicht schreiben: „Einstieg mitten im Kurs“. Stattdessen dezent: „Probetag – wann es Ihnen passt“, „Niveauwechsel möglich“, „Lernen ohne Druck“.

## Gute Themen für Deutsch-Tipps
Grammatik (Artikel, Kasus, Präpositionen, Perfekt/Präteritum, Nebensätze, Konjunktiv II), typische Fehler, Alltagswortschatz (Arzt, Amt, Wohnung, Arbeit, Einkaufen, Wetter, Verkehr), Redemittel (höflich bitten, Termine, Telefonieren, E-Mails), Aussprache, Prüfungstipps (telc, TestDaF, FSP), Redewendungen ohne Tabu-Bezug.
Bereits verwendet (nicht wiederholen): siehe `plan.json` (Titel).

## Werbethemen (rotieren, Fristen zuerst)
Intensivkurse A1–C1 (Starttermine!), FSP-Kurs Ärzte/Zahnärzte, FSP-Prüfungssimulation, telc-Termine des Folgemonats, telc-Preise, digitaler TestDaF (Anmeldefristen!), onSET, Einstufungstest (kostenlos, online), Probetag/Flexibilität, Privatunterricht, Crash-Kurs telc C1 Hochschule. Zuerst Einträge aus `reserve_werbung` verwenden.
Alle Fakten, Preise und Termine NUR aus `daten/`. Nichts erfinden. Fehlen Daten (z. B. telc nach Juni 2027), Thema meiden und in der Benachrichtigung darauf hinweisen.

## Gestaltung
- Grafiken mit `python3 tools/render.py spec.json` erzeugen (Stile: `werbung` = helles Creme/Teal-Design, `lernen` = dunkles Design, `reel` = Folienvideo 9:16). Bestehende Posts (`2026-11/`, `reels/*.json`) als Vorbild für Aufbau und Textmenge nehmen.
- Bilder anschließend ansehen (Read) und prüfen: kein Text abgeschnitten oder überlappend, nichts über den Fuß hinaus.
- Profilraster: Instagram zeigt Beiträge in der Profilübersicht als 3:4-Vorschau. Bei 4:5-Bildern (1080×1350) werden links und rechts je ca. 35 px abgeschnitten → wichtiger Inhalt mindestens 80 px vom seitlichen Rand. Bei Reel-Covern (1080×1920) werden oben und unten je ca. 240 px abgeschnitten → Titel/Hook auf der ersten Folie immer im mittleren Bereich (y 240–1680), nichts Wichtiges oben oder unten.
- Dateinamen: `JJJJ-MM/rbi-NN-stichwort.jpg|mp4`, NN = fortlaufende Post-Nummer.
- Für Reels die Folien zusätzlich als `reels/NN.json` speichern (für spätere Sprachaufnahme) und ein Sprechskript (1 Satz pro Folie) im Plan-Eintrag unter `sprechskript` ablegen.

## Karussell-Posts (mehrere Bilder)
- Hin und wieder, wenn das Thema es hergibt, einen Post als **Karussell** mit 3–6 Bildern anlegen (Instagram erlaubt 2–10). Gut geeignet: Wortschatz-Reihen, Schritt-für-Schritt-Grammatik, „5 typische Fehler“, Prüfungsablauf (telc/FSP), Vorher-Nachher-Sätze. Etwa 1 Karussell alle 2 Wochen, nicht öfter als 1 pro Woche.
- Bild 1 = Titelbild mit klarer Überschrift („Wischen ➜“ als kleiner Hinweis unten), danach je ein Punkt pro Bild, letztes Bild = Zusammenfassung oder Hinweis auf die RBI Sprachschule.
- Alle Bilder im selben Stil (`lernen` bzw. `werbung`), Format 4:5, Dateinamen `JJJJ-MM/rbi-NN-stichwort-1.jpg`, `-2.jpg` …
- Plan-Eintrag: typ "karussell", `bild_urls` (Liste in Reihenfolge), `bild_url` = erstes Bild (Titelbild).
- Vorlage: `karussell/17.json` (Stil `lernen`, Zähler „1/6“ oben rechts, „Wischen ➜“ auf Bild 1, zentrierter Inhalt mit größerer Schrift über den mitgelieferten <style>-Block). Neue Karussells als `karussell/NN.json` speichern.
- Facebook bekommt nur das Titelbild (bild_url) mit dem Text; im Facebook-Text die Punkte vollständig ausschreiben.

## Videos/Reels – NIEMALS ohne Ton
- Ein Reel/Video wird **nie** ohne Ton veröffentlicht. Neue Reels bekommen status "wartet_auf_ton" und erst nach eingebautem Sprachmemo (audio: true) status "geplant".
- Liegt bis zum Vortag 12 Uhr kein Memo vor, wird der Termin mit einem Lern-Post als Bild belegt; das Reel bleibt ohne Datum mit status "wartet_auf_ton" und wird eingeplant, sobald der Ton da ist.

## Sprachmemos
Sena lädt Aufnahmen nach `memos/NN.*` hoch (NN = Post-Nummer). Ein Reel mit vorhandenem Memo wird mit `render.py` (Feld `audio`) neu erzeugt und im Plan mit `"audio": true` markiert.
