
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    iframe_locator = (By.XPATH,"//iframe[@title='Widget containing checkbox for hCaptcha security challenge']")
    captcha_checkbox_locator = (By.XPATH, "//div[@id='checkbox']")

    def __init__(self, driver: webdriver.Chrome): 
        self.driver = driver
    
    def find(self, locator):
        elem = self.driver.find_element(*locator)
        return elem
    
    def find_list(self,locator):
        list_el = self.driver.find_elements(*locator)
        return list_el
    
    def find_with_scroll(self, locator):
        elem = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        return elem
    
    def click(self, locator):
        elem = self.find(locator)
        if elem:
            elem.click()

    def click_with_scroll(self, locator):
        elem = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        if elem:
            elem.click()
        

    def get_text(self, locator):
        txt = self.find(locator).text
        return txt
    
    def get_text_with_scroll(self,locator):
        txt = self.find_with_scroll(locator).text
        return txt

    def set(self, value, locator):
        self.find(locator).clear()
        self.find(locator).send_keys(value)
    
    def confirm_captcha(self):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(self.iframe_locator))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.captcha_checkbox_locator)).click()

    def get_attribute_value(self):
        el = self.driver.find_element(By.XPATH,"//input[@name='name']")
        result = el.get_attribute("value")
        return result
    

