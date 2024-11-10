import pytest
from tests.testData import TestData
from src.home_page import HomePage



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

    
    def test_search(self, initialize_driver):
        home_page = HomePage(initialize_driver)
        home_page.goto_main_page()
        search_result = home_page.search(TestData.search_product)
        product_found = search_result.check_first_result_correct(TestData.search_product)
        assert product_found, "Incorrect search result list"
        


    def test_add_to_chart(self,initialize_driver):
        home_page = HomePage(initialize_driver)
        home_page.goto_main_page()
        search_result = home_page.search(TestData.search_product)
        product_page = search_result.select_first_product_from_list()
        chart_page = product_page.add_product_to_chart()
        result = chart_page.search_product_in_chart(TestData.search_product)
        assert result, "expexted product is not in te chart"
