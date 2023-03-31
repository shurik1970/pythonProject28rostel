from pages.config import BASE_URL
from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from urllib.parse import urlparse


class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = BASE_URL
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find {locator}')

    def find_many_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not find {locator}')

    def find_element_until_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Element not clickable!')

    def find_visible_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f'Not find {locator}')

    def find_many_visible_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_element_located(locator),
                                                      message=f'Not find {locator}')

    def find_invisible_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f'Not find {locator}')

    def find_many_invisible_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_all_element_located(locator),
                                                      message=f'Not find {locator}')












# def wait_for_animation(web_browser, selector):
#     """
#     Waits until jQuery animations have finished for the given jQuery  selector.
#     """
#        WebDriverWait(web_browser, 10).until(lambda web_browser:  browser.execute_script(
#             'return jQuery(%s).is(":animated")' % json.dumps(selector))
#             == False)
#
#     def wait_for_ajax_loading(web_browser, class_name):
#         """
#         Waits until the ajax loading indicator disappears.
#         """
#         WebDriverWait(web_browser, 10).until(lambda web_browser: len(web_browser.find_elements_by_class_name(
#             class_name)) == 0)