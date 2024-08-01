from pages.home_page import HomePage
from pages.welcome_page import WelcomePage
from pages.bill_pay_page import BillPayPage
from pages.accounts_oveview_page import AccountOverviewPage
from pages.register_page import RegisterPage

def test_bill_pay(driver):
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

    welcome_page = WelcomePage(driver)

    #check balance
    welcome_page.got_to_account_overview()
    accounts_oveview_page = AccountOverviewPage(driver)
    old_total_balance = accounts_oveview_page.total_balance()

    # go to bay a bil page
    home_page.go_to_bill_pay()

    # pay a 100$ bill
    bill_pay_page = BillPayPage(driver)
    assert bill_pay_page.header_message() == "Bill Payment Service"

    account = 1
    amount = 100
    bill_pay_page.pay_bill(firstName, address, city, state, zipCode, phoneNumber, account, account, amount)
    assert bill_pay_page.header_message_result() == "Bill Payment Complete"

    #check balance
    welcome_page.got_to_account_overview()
    accounts_oveview_page = AccountOverviewPage(driver)
    new_total_balance = accounts_oveview_page.total_balance()

    assert (old_total_balance > new_total_balance) == True
    assert (old_total_balance - new_total_balance) == 100