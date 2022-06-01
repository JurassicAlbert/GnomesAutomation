import pytest

from actions.Login import Login
from actions.PlantWater import PlantWater


@pytest.mark.usefixtures("setup")
class WateringPlantsTest:

    def test_plants_watering(self):
        login = Login(self.driver)
        login.log_in_credential_pass()
        plant = PlantWater(self.driver)
        plant.select_watering_can()
        plant.water_plants()
