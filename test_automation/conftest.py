import configparser
from test_automation.pages.sl_login import SLLoginPage
import pytest
import allure
import os
import random

import string


def get_project_directory():
    """
    Returns the absolute path of the project directory.
    """
    return os.getcwd()


# Configuring the config.ini reader
def read_config():
    config_file_path = os.path.join(get_project_directory(),'test_automation', 'config.ini')
    print("MYPATH: "+str(config_file_path))
    config = configparser.RawConfigParser()
    config.read(config_file_path)
    return config


config = read_config()


def get_random_string(length=10):
    """
    Generates a random string of specified length using letters and digits.
    Args:
    - length (int): Length of the string to generate.

    Returns:
    - str: Randomly generated string.
    """
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return random_string


def capture_screenshot_in_png(page):
    screenshot = page.screenshot()
    return screenshot


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_size": {
            "width": 1920,
            "height": 1080
        },
        "viewport": {
            "width": 1920,
            "height": 1080
        },
        "permissions": [
            "clipboard-read",
            "clipboard-write"
        ]
    }


@pytest.fixture(autouse=False)
def set_global_timeout(page) -> None:
    timeout = int(config.get('Data', 'GLOBAL_TIMEOUT'))
    page.set_default_timeout(timeout)


@pytest.fixture(scope='session', autouse=True)
def get_credentials():
    d = dict()
    d['username'] = config.get('Data', 'USERNAME_SL')
    d['password'] = config.get('Data', 'PASSWORD_SL')
    return d


@pytest.fixture(autouse=True)
def login_to_sl(page):
    login_page = SLLoginPage(page)
    login_page.load()
    login_page.login(config.get('Data', 'USERNAME_SL'), config.get('Data', 'PASSWORD_SL'))


@pytest.fixture()
def test_data():
    dictionary = dict()
    dictionary['product_name'] = "Sauce Labs Backpack"
    return dictionary


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = 'allure-results'


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        # Attach a screenshot if the test fails
        if result.failed:
            if hasattr(item, 'instance') and hasattr(item.instance, 'page'):
                allure.attach(item.instance.page.screenshot(), name='screenshot',
                              attachment_type=allure.attachment_type.PNG)
        # Log execution time
        allure.dynamic.description(f"Execution time: {result.duration:.2f} seconds")

