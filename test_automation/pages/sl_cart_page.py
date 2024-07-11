import allure
from test_automation.pages.base_page import BasePage

class SLCartPage(BasePage):
    """Cart page for Saucelabs website"""
    def __init__(self, page):
        super().__init__(page)
        self.url = "/cart.html"

        # Locators of common elements
        self.cart_link = self.page.locator("//a[@class='shopping_cart_link']")
        self.cart_count = self.page.locator("//span[@class='shopping_cart_badge']")
        self.burger_menu = self.page.locator("//button[@id='react-burger-menu-btn']")
        self.about_link = self.page.locator("//a[@id='about_sidebar_link']")
        self.logout_link = self.page.locator("//a[@id='logout_sidebar_link']")
        self.all_items_link = self.page.locator("//a[@id='inventory_sidebar_link']")
        self.close_burger_menu_button = self.page.locator("//button[@id='react-burger-cross-btn']")

        # Locators specific to cart page
        self.cart_sub_header = self.page.get_by_text("Your Cart")
        self.item_quantity = self.page.locator(".cart_quantity")
        self.item_price = self.page.locator("//div[@class='inventory_item_price']")
        self.remove_from_cart_button = self.page.locator("//button[.='Remove']")
        self.checkout_button = self.page.locator("//button[@id='checkout']")
        self.continue_shopping_button = self.page.locator("//button[@id='continue-shopping']")

    @allure.step("Removing item from the cart")
    def remove_item_from_cart(self):
        self.remove_from_cart_button.click()

    @allure.step("Checking if the product is in the cart")
    def is_product_in_cart(self, product_name):
        is_present = False
        if self.page.locator(f"//div[@data-test='inventory-item-name' and text()='{product_name}']").is_visible():
            is_present = True
        return is_present
