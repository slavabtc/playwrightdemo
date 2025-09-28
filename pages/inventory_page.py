from pages.base_page import BasePage

class InventoryPage(BasePage):
    product_items = ".inventory_item"
    product_names = ".inventory_item_name"
    product_prices = ".inventory_item_price"
    sort_dropdown = "[data-test='product-sort-container']"


    def get_product_count(self):
        return self.page.locator(self.product_items).count()

    def get_product_names(self):
        return [el.inner_text() for el in self.page.locator(self.product_names).all()]

    def get_product_prices(self):
        return [el.inner_text() for el in self.page.locator(self.product_prices).all()]
    def sort_by(self, option_value):
        self.logger.info(f"Selecting sort option: {option_value}")
        self.page.locator(self.sort_dropdown).wait_for(state="visible", timeout=5000)
        self.page.locator(self.sort_dropdown).select_option(option_value)

    def click_on_product_by_name(self, name: str):
        self.page.locator(f"text={name}").click()

    def add_product_to_cart_by_index(self, index: int):
        self.page.locator(".inventory_item button", has_text="Add to cart").nth(index).click()

    def remove_product_from_cart_by_index(self, index: int):
        self.page.locator(".inventory_item button", has_text="Remove").nth(index).click()

    def get_cart_count(self) -> int:
        cart_badge = self.page.locator(".shopping_cart_badge")
        return int(cart_badge.inner_text()) if cart_badge.is_visible() else 0

    def click_cart_icon(self):
        self.page.locator(".shopping_cart_link").click()

    def add_to_cart_by_index(self, index: int = 0):
        buttons = self.page.locator('[data-test^="add-to-cart-"]')
        buttons.nth(index).click()

    def add_to_cart_by_name(self, product_name: str):
        self.logger.info(f"Adding '{product_name}' to cart.")
        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        add_button = product.locator("button:has-text('Add to cart')")
        add_button.click()