from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("")

def test_Login(self):
    driver = self.driver
    username = "moderator@mitwork.net"
    password = "123456"
    emailID="loginform-email"
    passID="loginform-password"
    loginbuttonID="login-button"

    emailFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailID))
    passFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passID))
    loginButtonElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(loginbuttonID))

    emailFieldElement.clear()
    emailFieldElement.send_keys(username)
    passFieldElement.clear()
    passFieldElement.send_keys(password)
    loginButtonElement.click()



if __name__=='__main__':
    unittest.main()
