from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from actions.Login import Login


class Plant:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.regal_name = "//div[@id='regal_14']"
        self.garden_tile_name = 'gardenTile'
        self.plant_cursor_name = 'cursor-pflanzen-v'
        self.driver = driver

    def select_plant_seeds_with_higher_time(self):
        for i in range(1, 205):
            garden_tile_cursor = self.garden_tile_name + str(i) + '_cursor'
            self.wait.until(EC.element_to_be_clickable((By.ID, garden_tile_cursor)))
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver).move_to_element(field).perform()
            if self.plant_cursor_name in field.get_attribute('class'):
                field.click()

    def select_seeds_from_regal(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.regal_name)))
        self.driver.find_element(By.XPATH, self.regal_name).click()
