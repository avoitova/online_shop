from selenium.webdriver.common.by import By
from src.base_page import BasePage
from src.chart_page import ChartPage


class ProductPage(BasePage):

    buy_button = (By.XPATH, "//div[@class='button buy']")
    

    def __init__(self, driver):
        super().__init__(driver)
    
    
    def add_product_to_chart(self):
        self.driver.implicitly_wait(5) 
        self.click(self.buy_button)
        return ChartPage(self.driver)