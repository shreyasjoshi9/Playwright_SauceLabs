from playwright.sync_api import Locator, Page
from test_automation.pages.base_page import BasePage


class SLBasePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.burger_menu = self.page.locator("//button[@id='react-burger-menu-btn']")
        self.cart_link = self.page.locator("//a[@class='shopping_cart_link']")

    def open_burger_menu(self, **kwargs):
        self.burger_menu.click(**kwargs)
