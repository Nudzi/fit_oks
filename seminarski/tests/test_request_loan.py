from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.welcome_page_for_new_user import WelcomePafeForNewUser
from pages.welcome_page import WelcomePage
from pages.request_loan_page import RequestLoanPage
from pages.accounts_oveview_page import AccountOverviewPage

def test_request_loan(driver):
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    assert home_page.is_forgot_to_login_info_visible() == True
    assert home_page.is_register_visible() == True

    #register
    # clean data
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
    # go to loan page
    home_page.go_to_request_loan_page()

    #request a loan
    request_loan_page = RequestLoanPage(driver)
    assert request_loan_page.header_message() == "Apply for a Loan"

    amount = 100
    downPayment = 100
    request_loan_page.request_loan(amount, downPayment)

    assert request_loan_page.header_message_result() == "Loan Request Processed"

    #remember new account LOAN id
    newAccountNumber = request_loan_page.get_new_loan_account_number()

    #check the balance if account exists
    welcome_page.got_to_account_overview()
    account_overview_page = AccountOverviewPage(driver)
    wholeAccount = account_overview_page.find_element(newAccountNumber)

    assert wholeAccount.balance == "$100.00"
    assert wholeAccount.available_amount == "$100.00"
