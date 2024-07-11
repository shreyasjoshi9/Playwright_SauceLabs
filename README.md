**Sauce Labs Playwright Testing Framework**

This testing framework is designed to facilitate automated testing of web applications using Playwright in conjunction with Pytest and Allure for enhanced reporting. It's tailored for projects that require robust browser-based testing, offering detailed insights into test executions and outcomes.

**Features**

Playwright Integration: Utilize Playwright for reliable browser automation.

Pytest Support: Leverage Pytest for structuring tests and managing test dependencies.

Allure Reporting: Generate comprehensive test reports using Allure.

Cross-Browser Testing: Support for testing across multiple browsers.

Video Recording: Automatically record test sessions for debugging.

Customizable Test Environment: Configure browser context settings such as viewport dimensions and permissions.

**Getting Started**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

**Prerequisites**

Things you need to install the software and how to install them:

python -m pip install playwright 

pytest pytest-playwright allure-pytest

Installing
A step-by-step series of examples that tell you how to get a development environment running:

**Clone the Repository**

git clone https://github.com/shreyasjoshi9/playwright_saucedemo

**Install Dependencies**

Navigate to the project directory and install required Python packages:

Make sure Python 3.12.0 is installed.

pip install -r requirements.txt

Run Playwright Install

Ensure that all necessary browser binaries are installed:

playwright install

Running the Tests

Execute the tests using Pytest. This command will also generate an Allure report.

pytest --alluredir=/path/to/allure/results

After running the tests, you can view the Allure report by using:

allure serve /path/to/allure/results

Deployment

Add additional notes about how to deploy this on a live system if applicable.

**Built With**

Playwright - The web automation framework used

Pytest - The testing framework

Allure - Test reporting tool

**Authors:**

Shreyas Joshi

**License:**

This project is licensed under the TableCheck, Japan.
