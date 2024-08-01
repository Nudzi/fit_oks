from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferFundsPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)
    
    def header_message(self):
        header_message_locator = (By.XPATH, "//*[@id='showForm']/h1")
        message_text = self.wait.until(EC.element_to_be_clickable(header_message_locator))
        return message_text.text
    

    def transfer(self, amount, accountId):
        amount_field_locator = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="amount"]')
        amount_field = self.wait.until(EC.element_to_be_clickable(amount_field_locator))
        amount_field.click()
        amount_field.clear()
        amount_field.send_keys(amount)

        counter = 1
        while counter > 0:
            tbody_locator = (By.XPATH,f'//*[@id="toAccountId"]/option[{counter}]')
            object_id = self.wait.until(EC.element_to_be_clickable(tbody_locator))
            if (object_id.text == accountId):  
                object_id.click()
                counter = 0
            else: counter = counter + 1


        transfer_button = self.selenium_webdriver.find_element(By.XPATH, '//*[@id="transferForm"]/div[2]/input')
        transfer_button.click()