from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from actions.Login import Login


class PlantWater:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.watering_can_tool = "//div[@id='giessen']"
        self.garden_tile_name = 'gardenTile'
        self.water_cursor_name = 'cursor-giessen'
        self.driver = driver

    def water_plants(self):
        for i in range(1, 205):
            garden_tile_cursor = self.garden_tile_name + str(i) + '_cursor'
            self.wait.until(EC.element_to_be_clickable((By.ID, garden_tile_cursor)))
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver).move_to_element(field).perform()
            if self.water_cursor_name in field.get_attribute('class'):
                field.click()

    def select_watering_can(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.watering_can_tool)))
        self.driver.find_element(By.XPATH, self.watering_can_tool).click()
