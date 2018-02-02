from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
driver = webdriver.Firefox()

driver.get("https://dev.e-sauda.kz/login?entry_type=manual")

def LoginTo():
      comp = driver.find_element_by_id('loginform-email')
      comp.send_keys("leskhan001@gmail.com")
      comp.send_keys(Keys.TAB)
      pas = driver.find_element_by_id('loginform-password')
      pas.send_keys("123456")
      pas.send_keys(Keys.RETURN)
      assert("Открытые")
LoginTo()
