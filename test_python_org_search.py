import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://demo.e-sauda.com/")


def test_search_in_python_org():
        
     
        elem = driver.find_element_by_name("q")
        elem.send_keys("дом")
        elem.send_keys(Keys.RETURN)
        time.sleep(6)
    
def clearSearch():
        s = driver.find_element_by_id("search-clr-icon")
        s.click()
        time.sleep(3)
        elem = driver.find_element_by_name("q")
        elem.send_keys(Keys.RETURN)
test_search_in_python_org()
clearSearch()

