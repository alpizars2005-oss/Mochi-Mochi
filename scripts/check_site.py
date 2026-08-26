from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

REQUIRED_IDS = {"inicio", "menu", "ingredientes", "pedido", "ventas"}
REQUIRED_DATA_HOOKS = {
    "data-categories",
    "data-menu-grid",
    "data-cart-items",
    "data-cart-total",
    "data-whatsapp-order",
    "data-sales-table",
    "data-export-sales",
    "data-export-csv",
    "data-clear-sales",
}


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.data_hooks: set[str] = set()
        self.local_refs: set[str] = set()
        self.external_scripts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)

        for name, _ in attrs:
            if name.startswith("data-"):
                self.data_hooks.add(name)

        ref = values.get("src") if tag in {"script", "img"} else values.get("href")
        if not ref or ref.startswith(("#", "mailto:", "tel:")):
            return

        parsed = urlparse(ref)
        if parsed.scheme in {"http", "https"}:
            if tag == "script":
                self.external_scripts.append(ref)
            return

        if tag in {"script", "link"}:
            self.local_refs.add(ref.split("?", 1)[0].lstrip("./"))


def main() -> None:
    parser = SiteParser()
    parser.feed(INDEX.read_text(encoding="utf-8"))

    missing_ids = REQUIRED_IDS - parser.ids
    missing_hooks = REQUIRED_DATA_HOOKS - parser.data_hooks
    missing_files = sorted(ref for ref in parser.local_refs if not (ROOT / ref).is_file())

    errors: list[str] = []
    if missing_ids:
        errors.append(f"Missing required section ids: {sorted(missing_ids)}")
    if missing_hooks:
        errors.append(f"Missing JavaScript data hooks: {sorted(missing_hooks)}")
    if missing_files:
        errors.append(f"Missing local assets: {missing_files}")

    xlsx_scripts = [url for url in parser.external_scripts if "xlsx" in url.lower()]
    if xlsx_scripts and not all("xlsx@0.18.5" in url for url in xlsx_scripts):
        errors.append("SheetJS CDN reference must stay version-pinned to xlsx@0.18.5")

    if errors:
        raise SystemExit("\n".join(errors))

    print(
        f"Static contract OK: {len(parser.ids)} ids, "
        f"{len(parser.data_hooks)} data hooks, {len(parser.local_refs)} local assets."
    )


if __name__ == "__main__":
    main()
