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
