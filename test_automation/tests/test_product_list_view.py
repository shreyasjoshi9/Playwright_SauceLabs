import allure
import logging
from test_automation.utils.reporting import report_fail
from test_automation.pages.sl_product_list_page import SLProductListPage
from test_automation.pages.sl_cart_page import SLCartPage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

"""
Product list view related tests
"""


@allure.title("Test Navigation to Product List")
def test_go_to_product_list(page):
    """
    Test case to verify that navigating to the product list is successful.

    Args:
    page: The browser page instance from Playwright

    Asserts:
    Asserts that the user is redirected to the inventory page URL.
    """
    sl_product_list = SLProductListPage(page)
    sl_product_list.go_to_product_list()
    assert page.url == "https://www.saucedemo.com/inventory.html", report_fail(page,
                                                                               "User is not navigated to expected URL of product list view")



@allure.title("Add an Item to the Cart")
def test_add_an_item_to_cart(page, test_data):
    """
    Test case to verify adding a specific item to the shopping cart.

    Args:
    page: The browser page instance from Playwright
    test_data: Dictionary containing 'product_name'

    Asserts:
    Checks if the cart count is 1 and if the specific product is in the cart.
    """
    sl_product_list = SLProductListPage(page)
    sl_product_list.add_item_to_cart(test_data['product_name'])
    current_cart_count = sl_product_list.cart_count.inner_text()
    assert current_cart_count == "1", "Cart count is incorrect"
    sl_cart = SLCartPage(page)
    assert sl_cart.is_product_in_cart(test_data['product_name']), report_fail(page,
                                                                              f"{test_data['product_name']} not found in cart")



@allure.title("Navigate to About Section")
def test_go_to_about_section(page):
    """
    Test case to verify that clicking on the 'about' link navigates to the correct URL.

    Args:
    page: The browser page instance from Playwright

    Asserts:
    Asserts that the user is redirected to the Saucelabs about page URL.
    """
    sl_product_list = SLProductListPage(page)
    sl_product_list.open_burger_menu()
    sl_product_list.about_link.click()
    assert page.url == "https://saucelabs.com/", report_fail(page,
                                                             "User is not navigated to expected About section URL")



@allure.title("Logout from Product List")
def test_logout_from_product_list(page):
    """
    Test case to verify logout functionality from the product list view.

    Args:
    page: The browser page instance from Playwright

    Asserts:
    Asserts that the user is redirected to the login page after logging out.
    """
    sl_product_list = SLProductListPage(page)
    sl_product_list.open_burger_menu()
    sl_product_list.logout_link.click()
    assert page.url == "https://www.saucedemo.com/", report_fail(page, "User is not logged out as expected")



@allure.title("Remove an Item from the Cart")
def test_remove_an_item_from_cart(page, test_data):
    """
    Test case to verify the removal of a specific item from the cart.

    Args:
    page: The browser page instance from Playwright
    test_data: Dictionary containing 'product_name'

    Asserts:
    Asserts that the specified product is no longer found in the cart.
    """
    sl_product_list = SLProductListPage(page)
    sl_product_list.add_item_to_cart(test_data['product_name'])
    sl_product_list.click_on_cart()
    sl_cart = SLCartPage(page)
    sl_cart.remove_item_from_cart()
    assert not sl_cart.is_product_in_cart(test_data['product_name']), report_fail(page,
                                                                                  f"{test_data['product_name']} is still found in cart")