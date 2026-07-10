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

# Principles — music (deltas)

Follows the **vlad base**: `[[vlad-vault/principles|vlad-vault/principles]]` (object rules) +
`[[vlad-vault/vault-template|vlad-vault/vault-template]]` (structure & entry points). Only deltas
here.

## Deltas

- **Media by pointer.** Тяжёлые файлы живут в `../media/` (вне git); vault
  держит карточку-указатель (что это, где лежит, статус). Файл без карточки =
  потерянный файл.
- **Тексты песен** — авторский первоисточник → `../../vlad-life/texts/`
  (`trust: primary`); здесь — рабочие карточки трека со ссылкой на текст.
- **Language.** English for infra/canon; Russian for lyrics, живые заметки о
  треках и всё, что Влад читает как автор.
- **Наружу — через витрину.** Посты/релизы-анонсы публикует `danny-content/`
  по своей routing-table; домен готовит материал, не постит сам.
