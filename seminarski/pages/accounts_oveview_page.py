from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.overViewModel import OverviewModel

class AccountOverviewPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='showOverview']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    
    def find_element(self, accountNumber):
        counter = 1
        while counter > 0:
            tbody_locator = (By.XPATH, f'//*[@id="accountTable"]/tbody/tr[{counter}]/td[1]/a')
            object_id = self.wait.until(EC.element_to_be_clickable(tbody_locator))
            if (object_id.text == accountNumber):  
                object_balance_locator = (By.XPATH, f'//*[@id="accountTable"]/tbody/tr[{counter}]/td[2]')
                object_balance = self.wait.until(EC.element_to_be_clickable(object_balance_locator))

                object_availabe_balance_locator = (By.XPATH, f'//*[@id="accountTable"]/tbody/tr[{counter}]/td[3]')
                object_availabe_balance = self.wait.until(EC.element_to_be_clickable(object_availabe_balance_locator))

                overview_model = OverviewModel(object_id.text ,object_balance.text, object_availabe_balance.text)
                counter = 0
                return overview_model
            else: counter = counter + 1

    def total_balance(self):
        counter = 1
        while counter > 0:
            tbody_locator = (By.XPATH, f'//*[@id="accountTable"]/tbody/tr[{counter}]/td[1]')
            object_id = self.wait.until(EC.element_to_be_clickable(tbody_locator))
            if (object_id.text == "Total"):  
                object_balance_locator = (By.XPATH, f'//*[@id="accountTable"]/tbody/tr[{counter}]/td[2]')
                object_balance = self.wait.until(EC.element_to_be_clickable(object_balance_locator))
                object_balance_as_number = object_balance.text[1:]

                return float(object_balance_as_number)
            else: counter = counter + 1
