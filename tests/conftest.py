import pytest
from playwright.sync_api import sync_playwright





@pytest.fixture(scope="class")
def setup(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page= browser.new_page()
    request.cls.page = page
    page.goto("https://openlayers.org/en/latest/examples/popup.html")
    yield page

    ##teardown
    browser.close()
    playwright.stop()