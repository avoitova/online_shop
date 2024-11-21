import pytest
from tests.testData import TestData
from src.home_page import HomePage
from selenium import webdriver
import logging



#@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
  pass

class TestLogin(BaseTest):


  def test_login(self, initialize_driver, logger_creation):
    home_page = HomePage(initialize_driver)
    log = logger_creation
    log.debug('logout if needed')
    home_page.logout()
    signin = home_page.click_login()
    signin.enter_email(TestData.email)
    log.debug('correct email was entered')
    signin.enter_password(TestData.password)
    log.debug('correct password was entered')
    home_page.enter_account_page()
    actual_user_name = home_page.get_account_name()
    log.debug(f"account holder is {actual_user_name}")
    assert actual_user_name == TestData.expected_user_name, "Aelita is not logged in"
    

    
  def test_login_wrong_credentials(self, initialize_driver, logger_creation):
    home_page = HomePage(initialize_driver)
    log = logger_creation
    home_page.logout()
    signin = home_page.click_login()
    log.debug('incorrect email was entered')
    signin.enter_email(TestData.email_wrong)
    log.debug('correct password was entered')
    signin.enter_password(TestData.password)
    log.debug('check allert appearence')
    message = signin.check_wrong_credentials_popup()
    assert message, "No allert popup while loggin with wrong credentials"
