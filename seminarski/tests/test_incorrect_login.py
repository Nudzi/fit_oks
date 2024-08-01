from pages.home_page import HomePage

def test_incorrect_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    assert home_page.is_forgot_to_login_info_visible() == True
    assert home_page.is_register_visible() == True

    home_page.login("john", "wrongPassword")

    assert home_page.is_error_message_visible() == True
    assert home_page.error_message() == "The username and password could not be verified."
    # to check again if login button and register is still available

    assert home_page.is_forgot_to_login_info_visible() == True
    assert home_page.is_register_visible() == True
    assert home_page.is_login_visible() == True