import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("STANDARD_USER")
PASSWORD = os.getenv("PASSWORD")

def test_inventory_page_shows_products(page):
    # Login
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)
    time.sleep(1)

    # Check inventory page
    inventory = InventoryPage(page)
    assert inventory.get_product_count() == 6

    names = inventory.get_product_names()
    prices = inventory.get_product_prices()

    assert all(name.strip() != "" for name in names)
    assert all(price.startswith("$") for price in prices)

    time.sleep(1)

def test_sort_by_name_az(page):
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)
    time.sleep(1)

    inventory = InventoryPage(page)

    # Use correct locator
    dropdown = inventory.page.locator(inventory.sort_dropdown)
    dropdown.wait_for(state="visible", timeout=5000)
    print("Dropdown count:", dropdown.count())
    print("Is visible:", dropdown.is_visible())
    print("Inner HTML:", dropdown.inner_html())

    # Sort by name descending (Z to A)
    inventory.sort_by("za")
    time.sleep(1)

    names = inventory.get_product_names()
    assert names == sorted(names, reverse=True)


def test_sort_by_price_low_to_high(page):
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)
    time.sleep(1)

    inventory = InventoryPage(page)
    inventory.sort_by("lohi")
    time.sleep(1)

    prices = inventory.get_product_prices()
    numeric_prices = [float(p.replace('$', '')) for p in prices]
    assert numeric_prices == sorted(numeric_prices)