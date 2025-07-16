import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
])
def test_valid_login(page, username, password):
    login = LoginPage(page)
    login.load()
    login.login(username, password)


    assert page.url == "https://www.saucedemo.com/inventory.html"