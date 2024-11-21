import pytest
from tests.testData import TestData
from src.home_page import HomePage
from tests.test_login import BaseTest


class TestSearch(BaseTest):

   
   def test_search(self, initialize_driver):
      home_page = HomePage(initialize_driver)
      home_page.goto_main_page()
      search_result = home_page.search(TestData.search_product)
      product_found = search_result.check_first_result_correct(TestData.search_product)
      assert product_found, "Incorrect search result list"
   
