import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get(")


def test_auxilary():
        elem = driver.find_element_by_partial_link_text("Земельный участок")
        elem.click()
        time.sleep(6)
        main = driver.find_element_by_link_text("E-SAUDA")
        main.click()
def auctions():
    op = driver.find_element_by_link_text("Объявления")
    op.click()

def test_lang_switch():
    lan = driver.find_element_by_class_name('lang-switch')
    lan.click()
    time.sleep(5)
 
test_auxilary()
auctions()
test_lang_switch()


