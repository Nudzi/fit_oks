from pages.home_page import HomePage
from pages.welcome_page import WelcomePage
from pages.admin_page import AdminPage
from pages.register_page import RegisterPage
from pages.welcome_page_for_new_user import WelcomePafeForNewUser
from pages.accounts_oveview_page import AccountOverviewPage

def test_admin(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    assert home_page.is_register_visible() == True

    home_page.go_to_admin()
    admin_page = AdminPage(driver)
    admin_page.clean_data()

    #set new value in admin with 1k
    admin_page.set_new_balance_value(1000)

    # register one with old value
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

    #check balance
    welcome_page.got_to_account_overview()
    accounts_oveview_page = AccountOverviewPage(driver)
    old_total_balance = accounts_oveview_page.total_balance()
    assert old_total_balance == 1000

    #set new value in admin with 2k
    home_page.go_to_admin()
    admin_page.set_new_balance_value(2000)

    # first logout
    welcome_page.log_out()

    # register new member with new value
    home_page.go_to_register_page()
    register_page = RegisterPage(driver)

    assert register_page.header_message() == 'Signing up is easy!'

    username2 = "username-test-2"
    password2 = "password-test-2"
    register_page.register(firstName, lastName, address, city, state, zipCode, phoneNumber, ssn, username2, password2, password2)
    
    welcome_page_for_new_user = WelcomePafeForNewUser(driver)
    assert welcome_page_for_new_user.header_message() == f"Welcome {username2}"
    assert welcome_page_for_new_user.info_message() == "Your account was created successfully. You are now logged in."

    welcome_page = WelcomePage(driver)

    assert welcome_page.is_logout_link_visible() == True
    assert welcome_page.is_account_name_visible() == f"Welcome {firstName} {lastName}"
    assert welcome_page.is_login_link_invisible() == True
    assert welcome_page.is_register_invisible() == True

    #check balance
    welcome_page.got_to_account_overview()
    accounts_oveview_page = AccountOverviewPage(driver)
    old_total_balance = accounts_oveview_page.total_balance()
    assert old_total_balance == 2000
