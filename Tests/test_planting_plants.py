import pytest

from actions.Login import Login
from actions.Plant import Plant


@pytest.mark.usefixtures("setup")
class PlantingPlantsTest:

    def test_plants_planting(self):
        login = Login(self.driver)
        login.log_in_credential_pass()
        plant = Plant(self.driver)
        plant.select_seeds_from_regal()
        plant.select_plant_seeds_with_higher_time()
