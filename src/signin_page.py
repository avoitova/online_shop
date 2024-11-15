from selenium.webdriver.common.by import By
from src.base_page import BasePage


class SignInPage(BasePage):


    login_field = (By.ID, 'login')
    password_field = (By.ID, 'pw')
    signin_button = (By.XPATH,"//button[contains(text(),'logga in')]")
    wrong_credentials_popup = (By.XPATH, "//div[@class='forgot-pass-link']")
    

   

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, value):
        self.set(value, self.login_field)

    def enter_password(self, value):
        self.set(value, self.password_field)
        self.click(self.signin_button)
        return BasePage(self.driver)
    
    def check_wrong_credentials_popup(self):
        message = self.find(self.wrong_credentials_popup).text
        return message
        

    