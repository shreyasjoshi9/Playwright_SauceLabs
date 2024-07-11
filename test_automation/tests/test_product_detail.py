import allure
import test_automation.utils.reporting as report
from test_automation.pages.sl_product_list_page import SLProductListPage
from test_automation.pages.sl_cart_page import SLCartPage
from test_automation.pages.sl_product_detail_page import SLProductDetailPage
import logging

"""
Product detail view related tests
"""
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

@allure.description("Verify that user is able to go to product deta after login")
def test_add_to_cart_from_product_detail_view(page, test_data):
    sl_product_list = SLProductListPage(page)
    sl_product_list.go_to_product_detail(test_data['product_name'])
    sl_product_detail = SLProductDetailPage(page)
    sl_product_detail.add_to_cart_product_detail.click()
    sl_cart = SLCartPage(page)
    assert sl_cart.is_product_in_cart(test_data['product_name']), report.report_fail(page, f"{test_data['product_name']} not found in cart")



@allure.description("Verify that user is able to add to cart from product detail view")
def test_price_and_name_from_product_detail_view(page, test_data):
    sl_product_list = SLProductListPage(page)
    list_view_price=sl_product_list.get_price_of_product(test_data['product_name'])
    sl_product_list.go_to_product_detail(test_data['product_name'])
    sl_product_detail = SLProductDetailPage(page)
    detail_view_price=sl_product_detail.get_price_of_product()
    detail_view_name=sl_product_detail.get_name_of_product()
    assert list_view_price==detail_view_price, report.report_fail(page, "List view price mismatch with detail view")
    assert test_data['product_name']==detail_view_name, report.report_fail(page, "List view name mismatch with detail view")
