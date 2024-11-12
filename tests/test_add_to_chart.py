import pytest
from tests.testData import TestData
from src.home_page import HomePage
from tests.test_login import BaseTest



class TestAddToChart(BaseTest):

   
   def test_add_to_chart(self,initialize_driver):
      home_page = HomePage(initialize_driver)
      home_page.goto_main_page()
      search_result = home_page.search(TestData.search_product)
      product_page = search_result.select_first_product_from_list()
      chart_page = product_page.add_product_to_chart()
      result = chart_page.search_product_in_chart(TestData.search_product)
      assert result, "expexted product is not in te chart"
   
