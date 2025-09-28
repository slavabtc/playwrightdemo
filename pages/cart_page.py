from pages.base_page import BasePage

class CartPage(BasePage):
    cart_title = ".title"
    cart_items = ".cart_item"
    checkout_button = '[data-test="checkout"]'

    def is_cart_page_loaded(self) -> bool:
        return self.is_visible(self.cart_title) and "Your Cart" in self.get_text(self.cart_title)

    def get_cart_item_count(self) -> int:
        return self.page.locator(self.cart_items).count()

    def click_checkout(self):
        self.click(self.checkout_button)

    def remove_item_by_name(self, product_name: str):
        item = self.page.locator(".cart_item").filter(has_text=product_name)
        remove_btn = item.locator("button:has-text('Remove')")
        remove_btn.click()