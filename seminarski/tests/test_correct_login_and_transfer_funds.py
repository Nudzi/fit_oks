from pages.home_page import HomePage
from pages.welcome_page import WelcomePage
from pages.new_account_page import NewAccountPage
from pages.account_details_page import AccountDetailsPage
from pages.transfer_funds_page import TransferFundsPage
from pages.accounts_oveview_page import AccountOverviewPage

def test_correct_login_and_transfer_funds(driver):
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    assert home_page.is_forgot_to_login_info_visible() == True
    assert home_page.is_register_visible() == True

    home_page.login("john", "demo")

    assert welcome_page.is_accounts_overview_visible() == True
    assert welcome_page.is_account_name_visible() == "Welcome John Smith"

    new_account_page = NewAccountPage(driver)
    welcome_page.go_to_new_account()

    assert new_account_page.header_message() == "Open New Account"
    assert new_account_page.is_new_account_visible() == True
    new_account_page.select_account_type()
    new_account_page.select_account_number()

    new_account_page.create_new_account()

    assert new_account_page.new_account_message_success() == "Congratulations, your account is now open."

    accountNumber = new_account_page.new_account_number()
    print(accountNumber)
    new_account_page.got_to_new_account()

    account_details_page = AccountDetailsPage(driver)
    assert account_details_page.header_message() == "Account Details"

    #check account overview
    welcome_page.got_to_account_overview()
    account_overview_page = AccountOverviewPage(driver)
    my_new_acount = account_overview_page.find_element(accountNumber)
    assert my_new_acount.id == accountNumber
    assert my_new_acount.balance == "$100.00"
    assert my_new_acount.available_amount == "$100.00"

    #lets transfer funds
    welcome_page.go_to_transfer_funds()
    transfer_funds_page = TransferFundsPage(driver)
    transfer_funds_page.transfer(100, my_new_acount.id)
    assert transfer_funds_page.header_message() == "Transfer Funds"

    #check account overview again after funding
    #otici nazad i provjeriti jel se vrijednost uvecala za sumu
    welcome_page.got_to_account_overview()
    account_overview_page = AccountOverviewPage(driver)
    my_existing_acount = account_overview_page.find_element(accountNumber)
    assert my_existing_acount.id == accountNumber
    assert my_existing_acount.balance == "$200.00"
    assert my_existing_acount.available_amount == "$200.00"

