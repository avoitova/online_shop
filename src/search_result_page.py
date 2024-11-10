from selenium.webdriver.common.by import By
from src.base_page import BasePage
from src.product_page import ProductPage

class SearchResultPage(BasePage):

    first_product_name = (By.XPATH, "(//div[@class='info-product-wrapper']/a[@class='simple-slider-list__name'])[1]")
    first_product_description = (By.XPATH, "(//div[@class='info-product-wrapper']/div[@class='simple-slider-list__description'])[1]")
    

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_product_name(self):
        self.driver.implicitly_wait(5) 
        name = self.get_text_with_scroll(self.first_product_name).casefold()
        description = self.get_text_with_scroll(self.first_product_description).casefold()
        print(name, description)
        return name, description
    
    def check_first_result_correct(self, product):
        first_list_item = self.get_first_product_name()
        print(first_list_item[0])
        if product.casefold() in first_list_item[0]:
            return True
        else:
            if product.casefold() in first_list_item[1]:
                return True
            else: 
                return False
    
    def select_first_product_from_list(self):
        self.driver.implicitly_wait(5) 
        self.click_with_scroll(self.first_product_name)
        return ProductPage(self.driver)
    