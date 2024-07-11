import allure
from test_automation.pages.base_page import BasePage


class SLLoginPage(BasePage):
    """Login page for SauceDemo website"""
    def __init__(self, page):
        super().__init__(page)

        self.username_input = self.page.locator("//input[@id='user-name']")
        self.password_input = self.page.locator("//input[@id='password']")
        self.login_button = self.page.locator("//input[@id='login-button']")
        self.login_error = self.page.locator("//h3[//@data-test='error']")

    @allure.step("Logging into Sauce Labs")
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
