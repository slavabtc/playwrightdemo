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