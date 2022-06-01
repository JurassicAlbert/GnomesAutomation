import time

import pytest

from Logging.test_login import LoginTest
from actions.Collect import Collect
from actions.Login import Login


@pytest.mark.usefixtures("setup")
class CollectingPlantsTest:

    def test_plants_collecting(self):
        login = Login(self.driver)
        login.log_in_credential_pass()
        collect = Collect(self.driver)
        collect.select_scythe()
        collect.collect_ripe_crops()
