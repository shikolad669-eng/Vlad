---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-10
updated: 2026-07-10
tags: [principles, conventions, deltas]
related:
  - ../../vlad-vault/principles
  - ../../vlad-vault/vault-template
---

# Principles — drafting (deltas)

Follows the **vlad base**: [[vlad-vault/principles|vlad-vault/principles]] +
[[vlad-vault/vault-template|vlad-vault/vault-template]]. Only deltas here.

## Deltas

- **No `market/` zone** — черчение (пока) не бизнес; template's mandatory
  `market/` is dropped by this delta. Появится клиентский спрос — заводим
  `market/` + `clients/` от факта.
- **`drawings/` zone added** — каталог чертежей: один файл = один чертёж/деталь,
  имя = search-hook. Карточка держит *что это, где файл (в `cad/`), версия,
  назначение* — не сам чертёж.
- **Тяжёлые файлы в домене (`cad/`), не в `documents/`.** Чертежи — собственный
  выход домена (как `music/media/`), поэтому живут в `drafting/cad/` (вне git),
  не во внешнем приёмнике `~/vlad/documents/`.
- **Версии — в имени файла, не в git.** git тяжёлые CAD-бинарники не хранит;
  версия кодируется суффиксом (`-v2`) и фиксируется в карточке.
- **Language.** Карточки/заметки — на языке, на котором Влад думает о детали;
  infra — English (base rule).
