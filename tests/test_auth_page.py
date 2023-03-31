
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from pages.setting import valid_phone, valid_login, valid_password, valid_ls, valid_email, valid_password_confirm


BASE_URL = "https://b2c.passport.rt.ru"

def test_Auth_Page(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL)
   search_form = driver.find_element(By.ID, 'username')
   search_form.send_keys(valid_phone)
   search_form = driver.find_element(By.ID, 'password')
   search_form.send_keys(valid_password)
   search_btn = driver.find_element(By.ID, 'kc-login').click()





def test_forgot_pass(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL)
   search_form = driver.find_element(By.ID, 'forgot_password').click
   driver.get(BASE_URL + '/auth/realms/b2c/login-actions/reset-credentials')



def test_user_agreement(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL + '/sso-static/agreement/agreement.html')



def test_switch_between_form(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL)
   search_form = driver.find_element(By.ID, 'username')
   search_form.send_keys(valid_phone)
   if valid_phone == valid_phone:
      assert driver.find_element(By.ID, 't-btn-tab-phone').text == 'Телефон'
   elif valid_phone == valid_email:
      assert driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').text == 'Почта'
   elif valid_phone == valid_login:
      assert driver.find_element(By.ID, 't-btn-tab-login').text == 'Логин'
   elif valid_phone == valid_ls:
      assert driver.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счет не найден'
   search_form = driver.find_element(By.ID, 'password')
   search_form.send_keys(valid_password)


def test_dark_theme(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL)
   search_form = driver.find_element(By.ID, 't-btn-tab-mail')
   # create action chain object
   action = ActionChains(driver)
   #
   # # double click the item
   action.double_click(on_element = search_form)

   #
   # # perform the operation
   action.perform()


@pytest.mark.auth
def test_auth_page_input_phone(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL)
   page = driver.find_element(By.ID, 'username')
   page.send_keys(valid_phone)
   page = driver.find_element(By.ID, 'password')
   page.send_keys(valid_password)





@pytest.mark.auth
def test_auth_page_input_email(selenium_driver):
   driver = selenium_driver
   driver.get(BASE_URL)
   page = driver.find_element(By.ID, 'username')
   page.send_keys(valid_email)
   page = driver.find_element(By.ID, 'password')
   page.send_keys(valid_password)
   time.sleep(15)  # на случай появления Captcha, необходимости ее ввода вручную
   search_btn = driver.find_element(By.ID, 'kc-login').click()























