from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Notification:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.bonus_pack_window = "//div[@class='link closeButton']"
        self.cookie_accept_button = "//a[@class='cookiemon-btn cookiemon-btn-accept']"
        self.driver = driver


    def close_bonus_notification(self):
        # self.wait.until(EC.presence_of_element_located((By.ID, self.bonus_pack_window)))
        bonus_pack_window = self.driver.find_element(By.XPATH, self.bonus_pack_window)
        if bonus_pack_window.is_displayed():
            self.wait.until(EC.element_to_be_clickable((By.ID, self.bonus_pack_window)))
            bonus_pack_window.click()

    def close_cookie_notification(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.cookie_accept_button)))
        print(self.driver.find_element(By.XPATH, self.cookie_accept_button))
