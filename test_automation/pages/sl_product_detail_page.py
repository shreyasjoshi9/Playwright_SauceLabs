import allure
from test_automation.pages.base_page import BasePage

class SLProductDetailPage(BasePage):
    """SL Product Detail page"""
    def __init__(self, page):
        super().__init__(page)
        self.url = "/inventory.html"

        # Locators of common elements
        self.cart_link = self.page.locator("//a[@class='shopping_cart_link']")
        self.cart_count = self.page.locator("//span[@class='shopping_cart_badge']")
        self.sort_by_dropdown = self.page.locator("//select[@class='product_sort_container']")
        self.burger_menu = self.page.locator("//button[@id='react-burger-menu-btn']")

        # Locators specific to product details page
        self.add_to_cart_product_detail = self.page.locator("#add-to-cart")
        self.product_name = self.page.locator("//div[@data-test='inventory-item-name']")
        self.price = self.page.locator("//div[@class='inventory_details_price']")

    @allure.step("Adding to the cart")
    def click_add_to_cart(self):
        self.add_to_cart_product_detail.click()

    @allure.step("Fetching name of the product")
    def get_name_of_product(self):
        return self.product_name.inner_text()

    @allure.step("Fetching price of the product")
    def get_price_of_product(self):
        return self.price.inner_text()
