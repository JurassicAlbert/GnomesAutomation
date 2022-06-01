import time

import pytest

from actions.Login import Login


@pytest.mark.usefixtures("setup")
class LoginTest:

    def test_login_credentials(self):
        login = Login(self.driver)
        login.send_login()
        login.send_password()
        login.select_server()
        login.log_in()
