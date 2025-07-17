import time
from playwright.sync_api import TimeoutError

class BasePage:
    def __init__(self, page):
        self.page = page

    def log(self, message: str):
        print(f"[LOG] {message}")

    def goto(self, url: str):
        self.log(f"Navigating to {url}")
        self.page.goto(url)

    def click(self, locator: str, retries=2, timeout=5000):
        self.log(f"Clicking element: {locator}")
        for attempt in range(retries):
            try:
                self.page.locator(locator).wait_for(state="visible", timeout=timeout)
                self.page.locator(locator).click()
                return
            except TimeoutError:
                self.log(f"Retry {attempt + 1}/{retries} failed: {locator} not ready")
                time.sleep(1)
        raise Exception(f"Element {locator} not clickable after {retries} attempts.")

    def fill(self, locator: str, text: str, timeout=5000):
        self.log(f"Filling input {locator} with '{text}'")
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        self.page.locator(locator).fill(text)

    def is_visible(self, locator: str, timeout=3000) -> bool:
        try:
            self.page.locator(locator).wait_for(state="visible", timeout=timeout)
            visible = self.page.locator(locator).is_visible()
            self.log(f"Checked visibility of {locator}: {visible}")
            return visible
        except TimeoutError:
            self.log(f"Element {locator} not visible (timeout)")
            return False

    def get_text(self, locator: str) -> str:
        self.log(f"Getting text from {locator}")
        return self.page.locator(locator).inner_text()