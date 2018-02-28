from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
driver = webdriver.Firefox()

driver.get("https://dev.e-sauda.kz/login?entry_type=manual")
class TestingDEV(unittest.TestCase):
 def LoginTo():
      comp = driver.find_element_by_id('loginform-email')
      comp.send_keys("username")
      comp.send_keys(Keys.TAB)
      pas = driver.find_element_by_id('loginform-password')
      pas.send_keys("pass")
      pas.send_keys(Keys.RETURN)
      assert("Открытые")
      
if __name__ == '__main__':
    unittest.main()
