from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def go_to(self):
        self.selenium_webdriver.get("https://parabank.parasoft.com/")
        self.selenium_webdriver.maximize_window()

    def get_page_tile(self):
        return self.selenium_webdriver.title
    
    def login(self, username, password):
        username_field_locator = self.selenium_webdriver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[1]/input")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_webdriver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[2]/input")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_webdriver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[3]/input")
        login_button.click()

    def is_forgot_to_login_info_visible(self):
        forgot_to_login_locator = (By.XPATH, "//*[@id='loginPanel']/p[1]/a")
        try:
            self.wait.until(EC.element_to_be_clickable(forgot_to_login_locator))
            return True
        except TimeoutException:
            return False
        
    def is_register_visible(self):
        register_locator = (By.XPATH, "//*[@id='loginPanel']/p[2]/a")
        try:
            self.wait.until(EC.element_to_be_clickable(register_locator))
            return True
        except TimeoutException:
            return False
        
    def is_error_message_visible(self):
        error_message_locator = (By.XPATH, "//*[@id='rightPanel']/h1")
        try:
            self.wait.until(EC.element_to_be_clickable(error_message_locator))
            return True
        except TimeoutException:
            return False
        
    def error_message(self):
        error_message_locator = (By.XPATH, "//*[@id='rightPanel']/p")
        message_text = self.wait.until(EC.element_to_be_clickable(error_message_locator))
        return message_text.text
    

    def is_login_visible(self):
        login_locator = (By.XPATH, "//*[@id='loginPanel']/form/div[3]")
        try:
            self.wait.until(EC.element_to_be_clickable(login_locator))
            return True
        except TimeoutException:
            return False
    
    def go_to_register_page(self):
        register_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="loginPanel"]/p[2]/a')
        register_button.click()

    def go_to_forgot_login_info(self):
        forgot_login_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="loginPanel"]/p[1]/a')
        forgot_login_button.click()

    def go_to_admin(self):
        admin_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[6]/a')
        admin_button.click()

    def go_to_bill_pay(self):
        bill_pay_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[4]/a')
        bill_pay_button.click()

    def go_to_customer_care(self):
        customer_care_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="headerPanel"]/ul[2]/li[3]/a')
        customer_care_button.click()

    def go_to_request_loan_page(self):
        request_loan_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[7]/a')
        request_loan_button.click()

    def clean_data(self):
        self.go_to_admin()
        clean_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="rightPanel"]/table/tbody/tr/td[1]/form/table/tbody/tr/td[2]/button')
        clean_button.click()