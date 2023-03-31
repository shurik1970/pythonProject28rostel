from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
import time
import pytest
from pages.setting import invalid_firstname, invalid_lastname, invalid_phone, invalid_email, \
    invalid_password, invalid_password_confirm, \
    valid_phone, valid_login, valid_password, invalid_password_confirm, \
    valid_ls, valid_email, valid_password_confirm, firstname, lastname


# firstname = ("Иван")
# lastname = ("Иванов")
# phone = ("89991234567")
# email = ("VasyPupkin@mail.ru")
#
# password = ("GHk7679gjhk")
# password_confirm = ("GHk7679gjhk")

BASE_URL = "https://b2c.passport.rt.ru"



def test_Reg_Page(selenium_driver):
    driver = selenium_driver
    driver.get(BASE_URL)
    search_btn = driver.find_element(By.ID, 'kc-register').click()




def test_Reg_Form_Page(selenium_driver):
    driver = selenium_driver
    driver.get(BASE_URL)
    search_btn = driver.find_element(By.ID, 'kc-register').click()
    search_form = driver.find_element(By.NAME, "firstName")
    search_form.send_keys(firstname)
    search_form = driver.find_element(By.NAME, "lastName")
    search_form.send_keys(lastname)
    search_form = driver.find_element(By.ID, 'address')
    search_form.send_keys(valid_email)
    search_form = driver.find_element(By.ID, 'password')
    search_form.send_keys(valid_password)
    search_form = driver.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_form.send_keys(valid_password_confirm)
    search_btn = driver.find_element(By.XPATH, "//button[@name='register']").click()
    time.sleep(5)


def test_Neg_Reg_Form_Page(selenium_driver):
    driver = selenium_driver
    driver.get(BASE_URL)
    search_btn = driver.find_element(By.ID, 'kc-register').click()
    search_form = driver.find_element(By.NAME, "firstName")
    search_form.send_keys(invalid_firstname)
    search_form = driver.find_element(By.NAME, "lastName")
    search_form.send_keys(lastname)
    search_form = driver.find_element(By.ID, 'address')
    search_form.send_keys(valid_email)
    search_form = driver.find_element(By.ID, 'password')
    search_form.send_keys(valid_password)
    search_form = driver.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_form.send_keys(valid_password_confirm)
    search_btn = driver.find_element(By.XPATH, "//button[@name='register']").click()
    time.sleep(10)


    print('Необходимо заполнить поле кириллицей. От 2 до 30 символов')







