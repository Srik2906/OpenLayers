import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(params = ["chromium","firefox"],scope="class")
def setup(request):
    playwright = sync_playwright().start()
    browser_dict = {
        "chromium" : playwright.chromium,
        "firefox" : playwright.firefox
    }
    browser_type = browser_dict.get(request.param)
    browser = browser_type.launch(headless=True)
    page= browser.new_page()
    request.cls.page = page
    page.goto(os.getenv("OPENLAYERS_URL"))
    yield page

    ##teardown
    browser.close()
    playwright.stop()