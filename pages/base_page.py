from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(Ec.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(Ec.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(Ec.element_to_be_clickable(locator))
