from pages.config import BASE_URL
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By

import time
import pytest

phone = "89513313441"
email = "sanny70@mail.ru"
password = "Homework70"


def test_recovery_pass(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL)
   search_form = driver.find_element(By.ID, 'forgot_password').click
   driver.get(BASE_URL + '/auth/realms/b2c/login-actions/reset-credentials')
   search_form = driver.find_element(By.ID, 'username')
   search_form.send_keys(email)
   search_form = driver.find_element(By.ID, 'captcha')
   time.sleep(30)
   """Ввод символов с картинки"""

   search_form = driver.find_element(By.ID, 'reset').click()






