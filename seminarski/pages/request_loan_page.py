from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RequestLoanPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def header_message(self):
        header_message_locator = (By.XPATH, '//*[@id="requestLoanForm"]/h1')
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def header_message_result(self):
        header_message_locator = (By.XPATH, '//*[@id="requestLoanResult"]/h1')
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def request_loan(self, amount, downPayment):
        self.setInput(amount, "amount")
        self.setInput(downPayment, "downPayment")

        apply_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="requestLoanForm"]/form/table/tbody/tr[4]/td[2]/input')
        wait_apply_button = self.wait.until(EC.element_to_be_clickable(apply_button))
        wait_apply_button.click()

    def setInput(self, field, field_id_string):
        field_locator = (By.ID, field_id_string)
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        wait_field.click()
        wait_field.clear()
        wait_field.send_keys(field)

    def get_new_loan_account_number(self):
        field_locator = (By.ID, "newAccountId")
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        return wait_field.text


