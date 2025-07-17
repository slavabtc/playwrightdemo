from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_items = ".inventory_item"
        self.item_names = ".inventory_item_name"
        self.item_prices = ".inventory_item_price"

    def get_product_count(self):
        return self.page.locator(self.inventory_items).count()

    def get_all_product_names(self):
        return self.page.locator(self.item_names).all_inner_texts()

    def get_all_prices(self):
        return self.page.locator(self.item_prices).all_inner_texts()