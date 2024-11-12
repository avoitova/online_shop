import pytest
from tests.testData import TestData
from src.home_page import HomePage
from selenium import webdriver



#@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
  pass

class TestLogin(BaseTest):

    
    def test_login(self, initialize_driver):
        home_page = HomePage(initialize_driver)
        signin = home_page.click_login()
        signin.enter_email(TestData.email)
        signin.enter_password(TestData.password)
        home_page.enter_account_page()
        actual_user_name = home_page.get_attribute_value()
        assert actual_user_name == TestData.expected_user_name, "Aelita is not logged in"

    
