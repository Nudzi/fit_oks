from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.welcome_page_for_new_user import WelcomePafeForNewUser
from pages.welcome_page import WelcomePage

def test_register(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    assert home_page.is_register_visible() == True

    #clean data
    home_page.clean_data()
    
    home_page.go_to_register_page()
    register_page = RegisterPage(driver)

    assert register_page.header_message() == 'Signing up is easy!'

    username = "username-test"
    password = "password-test"
    firstName = "Test Name"
    lastName = "Test LastName"
    address = "Test Address"
    city = "Test City"
    state = "Test State"
    zipCode = "Test ZipCode"
    phoneNumber = "Test Phone Number"
    ssn = "Test SSN"
    register_page.register(firstName, lastName, address, city, state, zipCode, phoneNumber, ssn, username, password, password)
    
    welcome_page_for_new_user = WelcomePafeForNewUser(driver)
    assert welcome_page_for_new_user.header_message() == f"Welcome {username}"
    assert welcome_page_for_new_user.info_message() == "Your account was created successfully. You are now logged in."

    welcome_page = WelcomePage(driver)

    assert welcome_page.is_logout_link_visible() == True
    assert welcome_page.is_account_name_visible() == f"Welcome {firstName} {lastName}"
    assert welcome_page.is_login_link_invisible() == True
    assert welcome_page.is_register_invisible() == True