from playwright.sync_api import sync_playwright

def fetch_chapter(url, save_path="chapter1.txt", screenshot_path="screenshot.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text("body")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(content)
        page.screenshot(path=screenshot_path, full_page=True)
        browser.close()

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
fetch_chapter(url)
