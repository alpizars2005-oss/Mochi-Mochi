# Security and privacy notes

Mochi Mochi is a static browser application. It has no project-owned backend, account system, or cloud database.

## Data boundary

- Sales history is stored in the browser's `localStorage` on the device where the site is used.
- Exported CSV/XLSX files leave the browser only when the user explicitly downloads them.
- Orders are transferred to WhatsApp only when the user activates the WhatsApp order link.
- A public deployment should never contain private customer notes, exported sales files, credentials, API keys, or unpublished business records.

## Third-party content

The site currently loads product photography from Unsplash and a version-pinned SheetJS browser build from jsDelivr. Availability and privacy behavior of those resources are controlled by their respective providers.

## Reporting a security problem

Do not include customer information, sales exports, credentials, tokens, or other sensitive data in a public issue. A report should contain the minimum reproduction steps needed to demonstrate the problem and should use synthetic data whenever possible.

## Supported code

Security fixes target the current `main` branch. Historical commits and locally modified deployments may not receive fixes.
