import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WelcomePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)
    
    def is_login_link_invisible(self):
        login_link_locator = (By.XPATH, "//*[@id='loginPanel']/form")
        try:
            self.wait.until(EC.invisibility_of_element_located(login_link_locator))
            return True
        except TimeoutException:
            return False
        

    def is_logout_link_visible(self):
        logout_link_locator = (By.XPATH, "//*[@id='leftPanel']/ul/li[8]/a")
        try:
            self.wait.until(EC.element_to_be_clickable(logout_link_locator))
            return True
        except TimeoutException:
            return False
        
    
    def is_accounts_overview_visible(self):
        show_overview_locator = (By.XPATH, "//*[@id='showOverview']")
        try:
            self.wait.until(EC.element_to_be_clickable(show_overview_locator))
            return True
        except TimeoutException:
            return False
    
    def is_account_name_visible(self):
        welcome_text_locator = (By.XPATH, "//*[@id='leftPanel']/p")
        wait_welcome_text = self.wait.until(EC.element_to_be_clickable(welcome_text_locator))
        return wait_welcome_text.text
    
    def is_forgot_to_login_info_invisible(self):
        forgot_to_login_locator = (By.XPATH, "//*[@id='loginPanel']/p[1]/a")
        try:
            self.wait.until(EC.invisibility_of_element_located(forgot_to_login_locator))
            return True
        except TimeoutException:
            return False
        
    def is_register_invisible(self):
        register_locator = (By.XPATH, "//*[@id='loginPanel']/p[2]/a")
        try:
            self.wait.until(EC.invisibility_of_element_located(register_locator))
            return True
        except TimeoutException:
            return False
        
        
    def go_to_transfer_funds(self):
        transfer_funds_button = self.selenium_webdriver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[3]/a")
        transfer_funds_button.click()

    def go_to_new_account(self):
        new_account_button = self.selenium_webdriver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[1]/a")
        new_account_button.click()
        
    def got_to_account_overview(self):
        new_account_button = self.selenium_webdriver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[2]/a")
        new_account_button.click()

    def log_out(self):
        log_out_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[8]/a')
        log_out_button.click()

    def go_to_update_contact_info(self):
        button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[6]/a')
        button.click()
        time.sleep(1)

