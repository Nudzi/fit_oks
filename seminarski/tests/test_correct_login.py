from pages.home_page import HomePage
from pages.welcome_page import WelcomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    assert home_page.is_forgot_to_login_info_visible() == True
    assert home_page.is_register_visible() == True

    home_page.login("john", "demo")

    assert welcome_page.is_login_link_invisible() == True
    assert welcome_page.is_logout_link_visible() == True
    assert welcome_page.is_accounts_overview_visible() == True
    assert welcome_page.is_account_name_visible() == "Welcome John Smith"
    assert welcome_page.is_forgot_to_login_info_invisible() == True
    assert welcome_page.is_register_invisible() == True

