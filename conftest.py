import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utils.actions import open_loging_page, login
from utils.constants import VALID_USER, VALID_PASS, LOGIN_TEST_SETS

#* Fixture para manejar el navegador
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--log-level=3")  # 0=ALL, 3=ERRORS only
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_user(driver):
    open_loging_page(driver)
    login(VALID_USER, VALID_PASS, driver)
    return driver

@pytest.fixture(
        params=LOGIN_TEST_SETS, 
        ids =[
            "empty user and empty pass",
            "empty user and valid pass",
            "valid user and empty pass",
            "valid user and invalid pass",
            "invalid user and empty pass",
            "invalid user and valid pass",
            "invalid user and invalid pass",
        ])
def invalid_user(request):
    return request.param