import pytest
from selenium import webdriver
from tests.testData import TestData
import logging

@pytest.fixture(scope="session")
def initialize_driver():
    print("Init Driver")
    driver = webdriver.Chrome()
    driver.get(TestData.url)
    driver.maximize_window()
    yield driver
    print("Close Driver")
    driver.close()



@pytest.fixture(scope="session")
def logger_creation():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler('log_file.log')
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
    
    