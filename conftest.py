import time
import pytest
from selenium import webdriver
from selenium import webdriver as selenium_wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from time import sleep



EMAIL = "sanny70@mail.ru"
PASSWORD = "Homework70"



@pytest.fixture(autouse=True)
def selenium_driver(request):
    s = Service(r"/projects/chrome/chromedriver")
    chrome_options = Options()
    driver = selenium_wd.Chrome(service=s, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def driver_class(request):
    driver = request.config.getoption("driver")
    if driver is not None:
        return SUPPORTED_DRIVERS[driver]
    raise pytest.UsageError("--driver must be specified")

