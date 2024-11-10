import pytest
from selenium import webdriver
from tests.testData import TestData

@pytest.fixture(scope="class")
def initialize_driver():
    print("Init Driver")
    driver = webdriver.Chrome()
    driver.get(TestData.url)
    driver.maximize_window()
    yield driver
    print("Close Driver")
    driver.close()



