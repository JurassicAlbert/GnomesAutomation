import pytest
from actions.Clean import Clean
from actions.Login import Login


@pytest.mark.usefixtures("setup")
class CleanGardenTest:

    def test_cleaning_garden(self):
        login = Login(self.driver)
        login.log_in_credential_pass()
        clean = Clean(self.driver, 0)
        clean.clean_garden()
