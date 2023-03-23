from pages.img_page import ImgBasePage


class TestText:
    class TestTextBox:

        def test(self, driver):
            page = ImgBasePage(driver, 'https://ya.ru/')
            page.open()
            page.img_search()
