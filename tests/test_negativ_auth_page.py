from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
import termcolor

import ast
import pickle
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from pages.setting import invalid_firstname, invalid_lastname, invalid_phone, invalid_email, invalid_password, invalid_password_confirm, \
    valid_phone, valid_login, valid_password, valid_ls, valid_email, valid_password_confirm, firstname, lastname
from pages.locators import AuthLocators
from pages.auth_page import *
from pages.setting import *

BASE_URL = "https://b2c.passport.rt.ru"


def test_Auth_Page_phone_neg(selenium_driver):
    driver = selenium_driver
    driver.get(BASE_URL)
    page = driver.find_element(By.ID, 'username')
    page.send_keys(invalid_phone)
    page = driver.find_element(By.ID, 'password')
    page.send_keys(valid_password)
    time.sleep(20)
    search_btn = driver.find_element(By.ID, 'kc-login').click()
    error_mess = driver.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)

    assert isinstance(error_mess, object)
    assert not (error_mess.text == 'Неверный логин или пароль') and not (page.check_color(forgot_pass) == '#ff4f12')


def test_Auth_Page_email_neg(selenium_driver):
    driver = selenium_driver
    driver.get(BASE_URL)
    page = driver.find_element(By.ID, 'username')
    page.send_keys(invalid_email)
    page = driver.find_element(By.ID, 'password')
    page.send_keys(valid_password)
    time.sleep(20)
    """ввести капчу"""
    search_btn = driver.find_element(By.ID, 'kc-login').click()
    error_mess = driver.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)



