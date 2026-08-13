from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state='storage_state.json'
        )
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()