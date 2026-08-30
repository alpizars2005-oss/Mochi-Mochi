# Repository Improvement Plan

Date: 2026-08-26

## Goal

Raise Mochi Mochi from a working four-file static site to a small but maintainable production-style web project without changing the current ordering, local-sales, WhatsApp, export, theme, or menu behavior.

## Research baseline

- Keep the zero-framework architecture: it is appropriate for this project and avoids unnecessary dependencies.
- Add automated structural checks instead of introducing a build tool only for CI.
- Preserve browser-local sales storage and the existing destructive-action confirmation.
- Improve accessibility and resilience conservatively, including reduced-motion handling and explicit JavaScript syntax validation.

## Atomic commit plan

1. Document the repository audit and intended changes.
2. Add repository hygiene and static CI checks.
3. Improve accessibility/resilience without changing business behavior.
4. Refresh README documentation and verification instructions.

## Validation

- Parse `index.html` with the Python standard library and verify required sections/data hooks.
- Run `node --check app.js` in CI.
- Verify local links and script/style references resolve to repository files.
- Preserve the existing WhatsApp order flow, localStorage sales key, export hooks, and confirmation before clearing sales.

## Risk / rollback

Low risk. The planned behavioral change is limited to accessibility/resilience CSS/HTML. No framework or runtime dependency will be added. Each implementation commit can be reverted independently.

---

## Audit follow-up — sales storage safety (2026-08-30)

### Findings

- Sales notes are user-controlled text and persisted in `localStorage`.
- `renderSales()` currently interpolates persisted notes/items directly into `innerHTML`; malformed/tampered local storage can therefore inject markup and can also crash rendering when the stored schema is incomplete.
- Export/WhatsApp behavior can remain unchanged while rendering is hardened.

### Atomic commit plan

1. Normalize persisted sales before they enter application state.
2. Escape persisted/user-controlled values before inserting them into sales-table HTML.
3. Extend the zero-dependency static checker with regression contracts for both protections.

### Validation

- `python scripts/check_site.py`
- `node --check app.js`
- Existing GitHub Actions static-site check.
- Manual: add a sale note containing `<b>test</b>` and confirm it displays literally, then reload and confirm the sale remains usable.

### Risk / rollback

Low risk and local to browser-side sales persistence/rendering. Existing valid sales remain compatible. Malformed entries are discarded instead of breaking the page; no storage key or export format changes.
