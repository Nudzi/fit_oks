from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='rightPanel']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def register(self, firstName, lastName, address, city, state, zipCode, phone, ssn, username, password, confirmPassword):
        self.setInput(firstName, "customer.firstName")
        self.setInput(lastName, "customer.lastName")
        self.setInput(address, "customer.address.street")
        self.setInput(city, "customer.address.city")
        self.setInput(state, "customer.address.state")
        self.setInput(zipCode, "customer.address.zipCode")
        self.setInput(phone, "customer.phoneNumber")
        self.setInput(ssn, "customer.ssn")
        self.setInput(username, "customer.username")
        self.setInput(password, "customer.password")
        self.setInput(confirmPassword, "repeatedPassword")

        register_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
        wait_register_button = self.wait.until(EC.element_to_be_clickable(register_button))
        wait_register_button.click()

    def setInput(self, field, field_id_string):
        field_locator = (By.ID, field_id_string)
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        wait_field.click()
        wait_field.clear()
        wait_field.send_keys(field)