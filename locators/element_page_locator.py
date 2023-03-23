from selenium.webdriver.common.by import By


class TextBasePageLocator:
    Search_text = (By.CSS_SELECTOR, "#text")
    Suggest_table = (By.CSS_SELECTOR, 'body > main > div.body__content > form')
    Link = (By.XPATH, '//*[@id="search-result"]/li[1]/div/div[2]/div[1]')


class ImgBasePageLocator:
    Img_link = (By.CSS_SELECTOR, 'body > main > div.services-pinned.i-bem.services-pinned_js_inited > div > a')
    Img_button = (By.XPATH, '/html/body/div[4]/div/div/div[1]/div/div[3]/div/span[13]')
    Category_img = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[1]')
    Category_img_text = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[1]')
    Open_first = (By.CSS_SELECTOR, 'body > div.page-layout.page-layout_page_search.page-layout_layout_serp.serp'
                                   '-controller.serp-controller_infinite_yes.serp-controller_navigation_yes.serp'
                                   '-controller_complain_yes.serp-controller_prefetch_yes.serp-controller_grid'
                                   '-counter.serp-controller_vertical-shadowed.serp-controller_viewer.serp'
                                   '-controller_viewer-history.serp-controller_small-top-padding.navigation'
                                   '-controller.incut-controller.i-bem.navigation-controller_js_inited.serp'
                                   '-controller_page_search.serp-controller_js_inited.incut-controller_js_inited.page'
                                   '-layout_js_inited > div.page-layout__column.page-layout__column_type_content > '
                                   'div > div.serp-controller__content > div')
    Check_img = (By.CSS_SELECTOR, 'body > div.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer > '
                                  'div.Modal-Wrapper > div > div > div > '
                                  'div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container > div > '
                                  'div.MediaViewer-TopSide.MediaViewer_theme_fiji-TopSide > '
                                  'div.MediaViewer-LayoutMain.MediaViewer_theme_fiji-LayoutMain > '
                                  'div.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene > '
                                  'div.MediaViewer-View.MediaViewer_theme_fiji-View')
    Button_right = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext > i')
    First_img = (By.CSS_SELECTOR, 'body > div.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer > '
                                  'div.Modal-Wrapper > div > div > div > '
                                  'div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container > div > '
                                  'div.MediaViewer-TopSide.MediaViewer_theme_fiji-TopSide > '
                                  'div.MediaViewer-LayoutMain.MediaViewer_theme_fiji-LayoutMain > '
                                  'div.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene > '
                                  'div.MediaViewer-View.MediaViewer_theme_fiji-View > div > div.MMImageContainer > '
                                  'img')
    Button_left = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev > i')
