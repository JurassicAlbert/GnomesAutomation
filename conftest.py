import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser-name', action='store', default='chrome'
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if browser_name == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    if browser_name == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
    if browser_name == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    if browser_name == 'opera':
        driver = webdriver.Opera(OperaDriverManager().install())

    driver.get('https://www.zieloneimperium.pl/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
