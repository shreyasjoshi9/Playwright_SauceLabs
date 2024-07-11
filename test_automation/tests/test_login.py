import allure
import logging
from test_automation.utils.reporting import report_fail
from test_automation.pages.sl_login import SLLoginPage
from test_automation import conftest

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

config = conftest.read_config()

@allure.title("Test Login Happy Flow")
@allure.description("Verify that user is able to login with valid credentials")
def test_login_happy_flow(page):
    """
    Test case to verify successful login with valid user credentials.

    Args:
    page: The browser page instance from Playwright

    Asserts:
    Asserts that after login, the user is redirected to the inventory page.
    """
    sl_login = SLLoginPage(page)
    sl_login.load()
    username = config.get('Data', 'USERNAME_SL')
    password = config.get('Data', 'PASSWORD_SL')
    sl_login.login(username, password)
    current_url = page.url
    assert current_url == "https://www.saucedemo.com/inventory.html", report_fail(page,
                                                                                  "User did not navigate to product list page after login")


@allure.title("Test Login Negative Flow")
def test_login_negative_flow(page):
    """
    Test case to verify login failure when using invalid credentials.

    Args:
    page: The browser page instance from Playwright

    Asserts:
    This should always fail and raise error in the reports (Assignment requirement).
    """
    sl_login = SLLoginPage(page)
    sl_login.load()
    sl_login.login(config.get('Data', 'INVALID_USERNAME_SL'), config.get('Data', 'PASSWORD_SL'))
    login_error_message = sl_login.login_error.inner_text()
    assert login_error_message == "Epic sadface: Username and password do not match any user in this service", report_fail(
        page, "Login error message is either incorrect or not displayed")
    current_url = page.url
    assert current_url == "https://www.saucedemo.com/inventory.html", report_fail(page,
                                                                                  "Login failed due to invalid credentials")

