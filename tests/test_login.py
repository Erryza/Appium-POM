import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self, setup):
        login_page = LoginPage(setup)

        login_page.option_btn()
        login_page.input_email("admin@gmail.com")
        login_page.input_password("admin123")
        login_page.click_btn()
