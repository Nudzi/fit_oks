from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def clean_data(self):
        clean_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="rightPanel"]/table/tbody/tr/td[1]/form/table/tbody/tr/td[2]/button')
        clean_button.click()


    def set_new_balance_value(self, newBalance):
        field_locator = (By.ID, 'initialBalance')
        wait_field = self.wait.until(EC.element_to_be_clickable(field_locator))
        wait_field.click()
        wait_field.clear()
        wait_field.send_keys(newBalance)

        submit_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="adminForm"]/input')
        submit_button.click()

