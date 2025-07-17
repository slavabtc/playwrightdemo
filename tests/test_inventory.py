import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time


def test_inventory_page_shows_products(page):
    # Login
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    time.sleep(1)

    # Check inventory page
    inventory = InventoryPage(page)
    assert inventory.get_product_count() == 6

    names = inventory.get_all_product_names()
    prices = inventory.get_all_prices()

    assert all(name.strip() != "" for name in names)
    assert all(price.startswith("$") for price in prices)

    time.sleep(1)