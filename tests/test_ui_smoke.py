import pathlib
from playwright.sync_api import sync_playwright


def test_ui_smoke():
    html = pathlib.Path("web/index.html").resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html)
        assert "Quality Pipeline Demo" in page.inner_text("h1")
        browser.close()
