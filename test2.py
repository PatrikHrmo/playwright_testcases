from playwright.sync_api import sync_playwright

# This is to test if 
def test_click():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://www.uitestingplayground.com/")
        link = page.locator("a[href='/dynamicid']")
        link.click()
        import time
        time.sleep(5)
        assert page.url == "http://www.uitestingplayground.com/dynamicid"
        browser.close()