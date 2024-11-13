from src.base_page import BasePage
from src.signin_page import SignInPage
from selenium.webdriver.common.by import By
from src.search_result_page import SearchResultPage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class HomePage(BasePage):


    signin_button  = (By.XPATH, "//div[@class='header-office']")
    account_name = (By.XPATH, "//input[@id='name']/@value")
    account_page = (By.XPATH, "//a[@class='header-office authorized']")
    search_button = (By.XPATH, "//div[@class='search-button']")
    serch_field = (By.XPATH, "//input[@id='search-input']")
    logo_button = (By.XPATH, "//a[@class='logo with-slogan']")
    logout_button = (By.XPATH, "//a[contains(text(),'Logga ut')]")
    

    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        self.click(self.signin_button)
        return SignInPage(self.driver)
    
    
    def enter_account_page(self):
        self.driver.implicitly_wait(10) 
        self.click(self.account_page)

    
    def search(self, value):
        self.click(self.search_button)
        self.driver.implicitly_wait(5) 
        self.set(value, self.serch_field)
        self.find(self.serch_field).send_keys(Keys.ENTER)
        return SearchResultPage(self.driver)
    
    def goto_main_page(self):
        self.click(self.logo_button)

    def logout(self):
        try:
            elem = self.find(self.account_page)
            if elem:
                elem.click()
            elem = self.find(self.logout_button)
            if elem:
                elem.click()
        except NoSuchElementException:
            print("No logout needed")

        