import allure
from test_automation.pages.base_page import BasePage
class SLProductListPage(BasePage):
    """
    Page object model for the Sauce Labs Product List page. This class inherits from SLBasePage.
    It includes locators for UI elements and methods to interact with the product list page.
    """

    def __init__(self, page):
        """
        Initializes a new instance of the SLProductListPage class.
        Args:
        page: Instance of the page provided by Playwright's browser context.
        """
        super().__init__(page)
        self.url = "/inventory.html"
        self.initialize_locators()

    def initialize_locators(self):
        """Initializes all the web element locators used in the Product List Page."""
        self.cart_link = self.page.locator("//a[@class='shopping_cart_link']")
        self.cart_count = self.page.locator("//span[@class='shopping_cart_badge']")
        self.sort_by_dropdown = self.page.locator("//select[@class='product_sort_container']")
        self.burger_menu = self.page.locator("//button[@id='react-burger-menu-btn']")
        self.about_link = self.page.locator("//a[@id='about_sidebar_link']")
        self.logout_link = self.page.locator("//a[@id='logout_sidebar_link']")
        self.all_items_link = self.page.locator("//a[@id='inventory_sidebar_link']")
        self.close_burger_menu_button = self.page.locator("//button[@id='react-burger-cross-btn']")
        self.initialize_product_buttons()

    def initialize_product_buttons(self):
        """Initializes locators for the 'Add to Cart' buttons of all products."""
        self.add_to_cart_backpack = self.page.locator("//button[@id='add-to-cart-sauce-labs-backpack']")
        self.add_to_cart_bikelight = self.page.locator("#add-to-cart-sauce-labs-bike-light")
        self.add_to_cart_bolt_tshirt = self.page.locator("//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.add_to_cart_fleece_jacket = self.page.locator("//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        self.add_to_cart_onesie = self.page.locator("//button[@id='add-to-cart-sauce-labs-onesie']")
        self.add_to_cart_test_all_things_tshirt = self.page.locator(
            "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")

    @allure.step("Open the burger menu by clicking the menu button")
    def open_burger_menu(self, **kwargs):
        """Opens the burger menu by clicking the menu button."""
        self.burger_menu.click(**kwargs)

    @allure.step("Open the sort by dropdown to allow selection of sorting method")
    def open_sort_by_dropdown(self):
        """Opens the sort by dropdown to allow selection of sorting method."""
        self.sort_by_dropdown.click()

    @allure.step("Log out of the current session by clicking the logout link")
    def logout(self, **kwargs):
        """Logs out of the current session by clicking the logout link."""
        self.logout_link.click(**kwargs)

    @allure.step("Add an item to the cart by clicking the 'Add to Cart' button adjacent to the specified product")
    def add_item_to_cart(self, product_name):
        """Adds an item to the cart by clicking the 'Add to Cart' button adjacent to the specified product."""
        self.page.locator(
            f"//*[text()='{product_name}']/ancestor::div[contains(@class,'inventory_item_label')]/following-sibling::div//button").click()

    @allure.step("Navigate to the cart by clicking the cart link")
    def click_on_cart(self):
        """Navigates to the cart by clicking the cart link."""
        self.cart_link.click()

    @allure.step("Navigate to the product list by interacting with the burger menu and selecting the 'All Items' link")
    def go_to_product_list(self):
        """Navigates to the product list by interacting with the burger menu and selecting the 'All Items' link."""
        self.open_burger_menu()
        self.all_items_link.click()

    def get_all_product_names(self):
        """Retrieves all product names listed on the page."""
        product_names_locators = self.page.query_selector_all("//div[contains(@class,'inventory_item_name')]")
        names = [p.inner_text() for p in product_names_locators]
        return names

    @allure.step("Navigate to the details page of a specific product")
    def go_to_product_detail(self, product_name):
        """Navigates to the details page of a specific product."""
        self.page.locator(f"//*[text()='{product_name}']").click()

    @allure.step("Retrieve the price of the specified product from its detail page")
    def get_price_of_product(self, product_name):
        """Retrieves the price of the specified product from its detail page."""
        price = self.page.locator(
            f"//div[contains(@class, 'inventory_item_label')]//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]/following-sibling::div[contains(@class, 'pricebar')]//div[@data-test='inventory-item-price']").inner_text()
        return price
