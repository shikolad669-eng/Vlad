---
type: reference
status: active
sensitivity: private
scope: work
axis: agentic
date: 2026-07-06
updated: 2026-07-06
tags: [lessons, gates, grabli, video]
related:
  - ../HOME
  - ../method/streams
  - ../../processes/video-station
---

# Lessons — грабли, ставшие код-гейтами

Подтверждённые правила (rule + trigger), зашитые в код content-type — чтобы не возвращались из прозы.
Пороги/цифры — [[../../processes/video-station]]; память — `~/.claude/projects/.../memory/`.

- **контраст-структурный** — *trigger:* любой оверлей/плашка/обложка на HDR/пёстром фоне.
  *rule:* мерить контраст текст↔подложка **на ярчайшем кадре окна в коде**, подложка ≥92%, не «на
  глаз»; не прошёл floor → поднять непрозрачность до сборки. Память `overlay-contrast-structural`.
  Гейт: `contrast.py`.
- **рендерер-общий** — *trigger:* любой текст на видео/обложке/плашке. *rule:* один `maksi_plate`,
  **импорт, не переписывать из прозы** (стиль = композиция в коде, не набор констант). Память
  `style-is-shared-renderer`.
- **тонмап-первым** — *trigger:* iPhone HLG-источник + наложения. *rule:* HLG→SDR **до** плашек;
  цвет судить по закодированному mp4, не по PNG. `video-station` → «Порядок композа».
- **аудио-экспорт-стерео** — *trigger:* любой рил наружу. *rule:* **стерео** + −14…−16 LUFS + TP −1;
  голос mono → оба канала, проверять **L/R RMS равны** (no one-ear); −20/моно = «проблемы со звуком».
  Память `reel-audio-export-stereo-loudness`. Гейт: `astats` в `audio`.

Новая грабля с прогона → сначала строка здесь (rule + trigger + память), затем гейт в коде.
