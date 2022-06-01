import time
from config.UserData import UserData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Login:
    def __init__(self, driver):
        self.login_field = "//input[@id='login_user']"
        self.password_field = "//input[@id='login_pass']"
        self.select_field = "//select[@id='login_server']"
        self.login_to_server_field = "//input[@id='submitlogin']"
        self.user_data = UserData()
        self.driver = driver

    # steps
    def send_login(self):
        login_field = self.driver.find_element(By.XPATH, self.login_field)
        login_field.send_keys(self.user_data.user_login)

    def send_password(self):
        login_field = self.driver.find_element(By.XPATH, self.password_field)
        login_field.send_keys(self.user_data.user_password)

    def select_server(self):
        select = Select(self.driver.find_element(By.XPATH, self.select_field))
        select.select_by_value(self.user_data.user_server)

    def log_in(self):
        self.driver.find_element(By.XPATH, self.login_to_server_field).click()

    def log_in_credential_pass(self):
        self.send_login()
        self.send_password()
        self.select_server()
        self.log_in()
