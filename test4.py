from playwright.sync_api import sync_playwright

# This is to test if the specific text shows when hovering above the image.
def test_open():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://the-internet.herokuapp.com/hovers")
        image = page.locator("#content > div > div:nth-child(3) > img")
        image.hover()
        text = image.inner_text()
        assert text in "name: user1"
        browser.close()