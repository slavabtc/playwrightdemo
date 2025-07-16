import pytest
import time
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
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
    login.login("locked_out_user", "secret_sauce")
    time.sleep(1)

    # Assert error message is visible
    assert login.error_message.is_visible()
    assert "locked out" in login.error_message.text_content().lower()
    time.sleep(1)
