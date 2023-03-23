import time

from locators.element_page_locator import TextBasePageLocator
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class TextBasePage(BasePage):
    locators = TextBasePageLocator()

    def search_text(self):
        self.search_filed()
        self.suggest_visible()
        self.link_t()

    def search_filed(self):
        assert self.element_is_present(self.locators.Search_text), "Нет поля поиск"

    def suggest_visible(self):
        search_text = self.element_is_visible(self.locators.Search_text)
        search_text.send_keys('Тензор')
        time.sleep(3)
        assert self.element_is_visible(self.locators.Suggest_table), "Нет таблицы с подсказками (suggest)"
        search_text.send_keys(Keys.ENTER)

    def link_t(self):
        link_first = self.element_is_present(self.locators.Link).text
        if link_first != 'tensor.ru':
            raise Exception('Первая ссылка не tensor.ru')
