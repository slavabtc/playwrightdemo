import pytest
import time
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

# Load environment variables
load_dotenv()

STANDARD_USER = os.getenv("STANDARD_USER")
LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER")
PASSWORD = os.getenv("PASSWORD")

@pytest.mark.parametrize("username,password", [
    (STANDARD_USER, PASSWORD),
])
def test_valid_login(page, username, password):
    login = LoginPage(page)
    login.load()
    login.login(username, password)

    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_locked_out_user_login(page):
    login = LoginPage(page)
    login.load()
    time.sleep(1)
    login.login(LOCKED_OUT_USER, PASSWORD)
    time.sleep(1)

    assert login.is_visible(login.error_message)
    assert "locked out" in login.get_text(login.error_message).lower()
    time.sleep(1)