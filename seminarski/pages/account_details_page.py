from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AccountDetailsPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def new_account_available_balance(self):
        header_message_locator = (By.XPATH, "//*[@id='accountDetails']/table/tbody/tr[3]/td[2]")
        try:
            message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
            return message_text.get_attribute("innerText")
        except TimeoutException:
            return False
    
    def new_account_balance(self):
        header_message_locator = (By.ID, "balance")
        message_text = self.wait.until(EC.visibility_of_element_located(header_message_locator))
        return message_text
    
    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='accountDetails']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text