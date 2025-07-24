from playwright.sync_api import sync_playwright

# This is to test if the page opens in webkit, and that the correct URL is asserted as a prove that the correct page opened. It opens the browser and it imports time to close automatically.
def test_open():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://www.uitestingplayground.com/")
        import time
        time.sleep(5)
        assert page.url == "http://www.uitestingplayground.com/"
        browser.close()