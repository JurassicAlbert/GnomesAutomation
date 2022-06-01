import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Collect:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.scythe_tool = "//div[@id='ernten']"
        self.garden_tile_name = 'gardenTile'
        self.collect_cursor_name = 'cursor-ernten'
        self.driver = driver

    def select_scythe(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.scythe_tool)))
        self.driver.find_element(By.XPATH, self.scythe_tool).click()

    def collect_ripe_crops(self):
        # ActionChains(self.driver).move_to_element(element_to_hover_over).perform()
        # 1 - 204 / 36 - 194 available
        for i in range(1, 205):
            garden_tile_cursor = self.garden_tile_name + str(i) + '_cursor'
            self.wait.until(EC.element_to_be_clickable((By.ID, garden_tile_cursor)))
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver).move_to_element(field).perform()
            if field.get_attribute("alt") != '0' and self.collect_cursor_name in field.get_attribute('class'):
                field.click()
        # for i in range(36, 195):
        #     garden_tile_cursor = self.garden_tile_name + str(i) + '_cursor'
        #     self.wait.until(EC.element_to_be_clickable((By.ID, garden_tile_cursor)))
        #     field = self.driver.find_element(By.ID, garden_tile_cursor)
        #     ActionChains(self.driver).move_to_element(field).perform()
        #     if self.collect_cursor_name in field.get_attribute('class'):
        #         field.click()
