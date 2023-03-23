from pages.element_page import TextBasePage


class TestText:
    class TestTextBox:

        def test(self, driver):
            page = TextBasePage(driver, 'https://ya.ru/')
            page.open()
            page.search_text()
