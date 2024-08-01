from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BillPayPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def header_message(self):
        header_message_locator = (By.XPATH, '//*[@id="billpayForm"]/h1')
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def header_message_result(self):
        header_message_locator = (By.XPATH, '//*[@id="billpayResult"]/h1')
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def pay_bill(self, name, address, city, state, zipCode, phone, accountNumber, verifyAccount, amount):
        self.setInput(name, "payee.name")
        self.setInput(address, "payee.address.street")
        self.setInput(city, "payee.address.city")
        self.setInput(state, "payee.address.state")
        self.setInput(zipCode, "payee.address.zipCode")
        self.setInput(phone, "payee.phoneNumber")
        self.setInput(accountNumber, "payee.accountNumber")
        self.setInput(verifyAccount, "verifyAccount")
        self.setInput(amount, "amount")

        pay_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[14]/td[2]/input')
        wait_pay_button = self.wait.until(EC.element_to_be_clickable(pay_button))
        wait_pay_button.click()

    def setInput(self, field, field_id_string):
        field_locator = (By.NAME, field_id_string)
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        wait_field.click()
        wait_field.clear()
        wait_field.send_keys(field)
