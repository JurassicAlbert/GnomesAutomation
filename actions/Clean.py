import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Clean:
    __FIELD_SIZE = ['2.50', '50', '250', '500']

    # field_size: int from 0 to 4
    def __init__(self, driver, field_size_number):
        self.wait = WebDriverWait(driver, 10)
        self.money = "//span[@id='bar']"
        self.money_to_spend = "//span[@id='bar']"
        self.field_size = Clean.__FIELD_SIZE[field_size_number]
        self.field_common_name = 'feld'
        self.base_dialog_window_name = "//div[@id='baseDialogInner']"
        self.allow_button = "//div[contains(text(),'Tak')]"
        self.decline_button = "//div[contains(text(),'Nie')]"
        self.base_dialog_text = "//div[@id='baseDialogText']/div"
        self.driver = driver

    def clean_garden(self):
        field_to_clean = int(math.floor(self.check_money_to_spend() / float(self.field_size)))
        fields = self.driver.find_elements(By.CLASS_NAME, self.field_common_name)
        for field in fields:
            self.wait.until(EC.element_to_be_clickable(field))
            field.click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.base_dialog_window_name)))
            dialog_window = self.driver.find_element(By.XPATH, self.base_dialog_window_name)
            if dialog_window.is_displayed():
                if self.field_size in self.driver.find_element(By.XPATH, self.base_dialog_text).text:
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, self.allow_button)))
                    self.driver.find_element(By.XPATH, self.allow_button).click()
                    field_to_clean = field_to_clean - 1
            else:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.decline_button)))
                self.driver.find_element(By.XPATH, self.decline_button).click()

            if field_to_clean == 0:
                return

    def check_money_to_spend(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.money_to_spend)))
        money_to_spend = self.driver.find_element(By.XPATH, self.money_to_spend).text
        return self.remove_currency_from_value(money_to_spend)

    @staticmethod
    def remove_currency_from_value(value):
        value = value.split(' ')[0]
        value = value.replace(',', '.')
        return float(value)
