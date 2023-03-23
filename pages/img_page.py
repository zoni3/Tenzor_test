import time

from locators.element_page_locator import ImgBasePageLocator
from pages.base_page import BasePage
from urllib.parse import unquote


class ImgBasePage(BasePage):
    locators = ImgBasePageLocator()

    def img_search(self):
        self.menu_button()
        self.open_category()
        self.move_img()

    def menu_button(self):
        window_before = self.driver.window_handles[0]
        assert self.element_is_present(self.locators.Img_link), "Нет кнопки меню"
        menu_button = self.element_is_present(self.locators.Img_link)
        menu_button.click()
        img_button = self.element_is_present(self.locators.Img_button)
        img_button.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(2)
        assert 'https://yandex.ru/images/' == self.driver.current_url, "Вы находитесь на другой ссылке"

    def open_category(self):
        category_open = self.element_is_present(self.locators.Category_img)
        category_text = self.element_is_present(self.locators.Category_img_text).text
        category_open.click()
        time.sleep(4)
        category_search = unquote(self.driver.current_url).replace('https://yandex.ru/images/search?text=', '')
        category_search_red = category_search.split('&nl=1')
        assert category_search_red[0] == category_text, "Категория не совпадает"

    def move_img(self):
        self.element_is_present(self.locators.Open_first).click()
        time.sleep(3)
        assert self.element_is_present(self.locators.Check_img), 'Картинка не открылась'
        first_img = self.element_is_present(self.locators.First_img).get_attribute('src')
        self.element_is_present(self.locators.Button_right).click()
        second_img = self.element_is_present(self.locators.First_img).get_attribute('src')
        assert first_img != second_img, ' Картинка не изменилась'
        self.element_is_present(self.locators.Button_left).click()
        first_img_ever = self.element_is_present(self.locators.First_img).get_attribute('src')
        assert first_img == first_img_ever, 'Картинка не вернулась'

