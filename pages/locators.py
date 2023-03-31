from selenium.webdriver.common.by import By

BASE_URL = "https://b2c.passport.rt.ru"







class AuthLocators:
    AUTH_USERNAME = (By.ID, 'username')
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_FORM_ERROR = (By.XPATH, "//span[@id='form-error-message']")
    AUTH_MESS_ERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    AUTH_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    AUTH_REG_IN = (By.ID, 'kc-register')
    AUTH_ACTIVE_TAB = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')
    AUTH_REG_IN_TEMP_CODE = (By.ID, 'back_to_otp_btn')
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_EMAIL = (By.XPATH, '//*[@id="t-btn-tab-mail"]')
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_LS = (By.ID, 't-btn-tab-ls')



class RegLocators:
    """Локаторы страницы регистрации"""
    REG_FIRSTNAME = (By.NAME, "firstName")
    REG_LASTNAME = (By.NAME, "lastName")
    REG_REGION = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    REG_EMAIL_OR_PHONE = (By.ID, 'address')
    REG_PASSWORD = (By.ID, 'password')
    REG_PASS_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    REG_REGISTER = (By.XPATH, "//button[@name='register']")
    REG_CARD_MODAL = (By.XPATH, "//h2[@class='card-modal__title']")




class NewPassLocators:
    """Локаторы страницы восстановления пароля"""
    NEWPASS_ADDRESS = (By.ID, 'username')
    NEWPASS_BTN_CONTINUE = (By.ID, 'reset')
    NEWPASS_ONETIME_CODE = (By.XPATH, '//input[@inputmode="numeric"]')
    NEWPASS_NEW_PASS = (By.ID, 'password-new')
    NEWPASS_NEW_PASS_CONFIRM = (By.ID, 'password-confirm')
    NEWPASS_BTN_SAVE = (By.XPATH, '//button[@id="t-btn-reset-pass"]')