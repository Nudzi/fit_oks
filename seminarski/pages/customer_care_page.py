from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerCarePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='rightPanel']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def thank_you_note(self):
        header_message_locator = (By.XPATH, '//*[@id="rightPanel"]/p[1]')
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def send_request(self, name, email, phone, message):
        self.setInput(name, "name")
        self.setInput(email, "email")
        self.setInput(phone, "phone")
        self.setInput(message, "message")

        send_request_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input')
        wait_send_request_button = self.wait.until(EC.element_to_be_clickable(send_request_button))
        wait_send_request_button.click()

    def setInput(self, field, field_id_string):
        field_locator = (By.ID, field_id_string)
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        wait_field.click()
        wait_field.clear()
        wait_field.send_keys(field)