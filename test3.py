from playwright.sync_api import Page

def test_header(page: Page):
    page.goto("http://www.uitestingplayground.com/")
    header = page.locator("h1")
    header_text = header.inner_text()
    assert "UI Testing Playground" in header_text