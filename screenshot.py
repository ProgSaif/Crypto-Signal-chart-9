from playwright.sync_api import sync_playwright


def capture_chart(url, filename="chart.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto(url)

        # wait for chart to fully load
        page.wait_for_timeout(8000)

        page.screenshot(path=filename)

        browser.close()

    return filename
