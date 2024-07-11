import allure
import pytest
from allure_commons.types import AttachmentType


@allure.step("Step Passed :{0}")
def report_pass(message):
    with allure.step(f"Test Step Passed"):
        pass


@allure.step("Step Failed : {0}")
def report_fail(page, message):
    allure.attach(page.screenshot(path="screenshots/screenshot.png", full_page=True), name="fail_screenshot",
                  attachment_type=AttachmentType.PNG)
    pytest.fail(f"Test Step Failed : {message}")


@allure.step("Step Info : {0}")
def report_info(message):
    None