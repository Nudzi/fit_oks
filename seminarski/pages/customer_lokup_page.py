from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerLookupPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='rightPanel']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    

    def info_message(self):
        info_message_locator = (By.XPATH, '//*[@id="rightPanel"]/p')
        message_text = self.wait.until(EC.element_to_be_clickable(info_message_locator))
        return message_text.text
    
    def is_username_visbile(self):
        text_locator = (By.XPATH, '//*[@id="rightPanel"]/p[2]')
        wait_text = self.wait.until(EC.element_to_be_clickable(text_locator))
        return wait_text.text
    
    def find_my_login_info(self, firstName, lastName, address, city, state, zipCode, ssn):
        self.setInput(firstName, "firstName")
        self.setInput(lastName, "lastName")
        self.setInput(address, "address.street")
        self.setInput(city, "address.city")
        self.setInput(state, "address.state")
        self.setInput(zipCode, "address.zipCode")
        self.setInput(ssn, "ssn")

        register_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="lookupForm"]/table/tbody/tr[8]/td[2]/input')
        wait_register_button = self.wait.until(EC.element_to_be_clickable(register_button))
        wait_register_button.click()

    def setInput(self, field, field_id_string):
        field_locator = (By.ID, field_id_string)
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        wait_field.click()
        wait_field.clear()
        wait_field.send_keys(field)