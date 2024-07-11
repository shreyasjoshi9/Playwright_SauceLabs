from playwright.sync_api import Page

class BasePage:
    """Base Page"""
    def __init__(self, page: Page):
        self.url = "https://www.saucedemo.com/"
        self.page = page

    def load(self):
        self.page.goto(self.url)