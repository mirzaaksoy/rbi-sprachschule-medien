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

## Sprachmemos
Sena lädt Aufnahmen nach `memos/NN.*` hoch (NN = Post-Nummer). Ein Reel mit vorhandenem Memo wird mit `render.py` (Feld `audio`) neu erzeugt und im Plan mit `"audio": true` markiert.
