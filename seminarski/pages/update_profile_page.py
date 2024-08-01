from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class UpdateProfilePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='updateProfileForm']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def update_profile(self, firstName, lastName, address, city, state, zipCode, phone):
        self.setInput(firstName, "customer.firstName")
        self.setInput(lastName, "customer.lastName")
        self.setInput(address, "customer.address.street")
        self.setInput(city, "customer.address.city")
        self.setInput(state, "customer.address.state")
        self.setInput(zipCode, "customer.address.zipCode")
        self.setInput(phone, "customer.phoneNumber")

        update_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="updateProfileForm"]/form/table/tbody/tr[8]/td[2]/input')
        wait_update_button = self.wait.until(EC.element_to_be_clickable(update_button))
        wait_update_button.click()

    def setInput(self, field, field_id_string):
        field_locator = (By.ID, field_id_string)
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        wait_field.click()
        wait_field.clear()
        wait_field.send_keys(field)


    def is_input_field_available(self, field_id_string):
        locator = (By.ID, field_id_string)
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False
        
    def get_value_from_inputs(self, field_id_string):
        locator = (By.ID, field_id_string)
        try:
            message_text = self.wait.until(EC.element_to_be_clickable(locator))
            message_text.click()
            return message_text.get_property('value')
        except Exception:
            return False