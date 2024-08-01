from pages.home_page import HomePage
from pages.customer_care_page import CustomerCarePage

def test_customer_care(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "ParaBank | Welcome | Online Banking"
    
    home_page.go_to_customer_care()
    customer_care_page = CustomerCarePage(driver)
    assert customer_care_page.header_message() == "Customer Care"

    name = "Test Name"
    email = "test@test.com"
    phone = "Test Phone"
    message = "Test Message"
    customer_care_page.send_request(name, email, phone, message)

    assert customer_care_page.thank_you_note() == f"Thank you {name}"