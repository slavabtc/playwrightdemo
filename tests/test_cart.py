import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("STANDARD_USER")
PASSWORD = os.getenv("PASSWORD")

def test_cart_page_loads(page):
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_to_cart_by_index(0)
    time.sleep(1)
    inventory.click_cart_icon()

    cart = CartPage(page)
    assert cart.is_cart_page_loaded()

def test_cart_item_appears(page):
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_to_cart_by_index(0)
    time.sleep(1)
    inventory.click_cart_icon()

    cart = CartPage(page)
    assert cart.get_cart_item_count() == 1

def test_checkout_button_visible(page):
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_to_cart_by_index(0)
    time.sleep(1)
    inventory.click_cart_icon()

    cart = CartPage(page)
    assert cart.is_visible(cart.checkout_button)

def test_remove_item_from_cart(page):
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_to_cart_by_name("Sauce Labs Backpack")

    cart_icon = inventory.page.locator("#shopping_cart_container")
    cart_icon.click()

    cart = CartPage(page)
    assert cart.get_cart_item_count() == 1

    cart.remove_item_by_name("Sauce Labs Backpack")
    assert cart.get_cart_item_count() == 0