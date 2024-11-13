from src.base_page import BasePage
from selenium.webdriver.common.by import By


class ChartPage(BasePage):
    

    product_list = (By.XPATH, "//div[@class='product-list_product-item']")
    item_header_locator = (By.XPATH, "//div[@class='product-list_product-item']//div[@class='product__header']")
    item_descr_locator = (By.XPATH, "//div[@class='product-list_product-item']//div[@class='product__header-desc']")
    close_chart = (By.XPATH, "//div[@class='popup__window']//div[@class='popup-close close-icon']")


    def __init__(self, driver):
        super().__init__(driver)

    def search_product_in_chart(self, expected_text):
        items_header_list = self.find_list(self.item_header_locator)
        items_descr_list = self.find_list(self.item_descr_locator)
        for i in items_header_list:
            header = i.text
            if expected_text in header:
                return True
            else:
                continue
        for i in items_descr_list:
            descr = i.text
            if expected_text in descr:
                return True
            else:
                return False
    
    def close_crart(self):
        self.click(self.close_chart)