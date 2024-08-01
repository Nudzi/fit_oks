from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class NewAccountPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)
    
    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='openAccountForm']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def create_new_account(self):
        new_account_button = self.selenium_webdriver.find_element(By.XPATH, "//*[@id='openAccountForm']/form/div/input")
        message_text = self.wait.until(EC.element_to_be_clickable(new_account_button))
        return message_text.send_keys(Keys.ENTER)

    def new_account_message_info(self):
        header_message_locator = (By.XPATH, "//*[@id='openAccountForm']/form/p[2]/b")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def new_account_message_success(self):
        header_message_locator = (By.XPATH, "//*[@id='openAccountResult']/p[1]")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
        
    def new_account_number(self):
        header_message_locator = (By.ID, "newAccountId")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def got_to_new_account(self):
        new_account_button = self.selenium_webdriver.find_element(By.ID, "newAccountId")
        new_account_button.click()
    
    def select_account_type(self):
        header_message_locator = (By.XPATH, "//*[@id='type']/option[2]")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.click
    
    def select_account_number(self):
        header_message_locator = (By.XPATH, "//*[@id='fromAccountId']/option[1]")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.click
    
    def is_new_account_visible(self):
        register_locator = (By.XPATH, "//*[@id='openAccountForm']/form/div/input")
        try:
            self.wait.until(EC.element_to_be_clickable(register_locator))
            return True
        except TimeoutException:
            return False