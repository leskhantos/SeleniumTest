from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest
driver = webdriver.Firefox()

driver.get("https://dev.e-sauda.kz/login?entry_type=manual")
def LoginTo():
      comp = driver.find_element_by_id('loginform-email')
      comp.send_keys("user")
      comp.send_keys(Keys.TAB)
      pas = driver.find_element_by_id('loginform-password')
      pas.send_keys("pass")
      pas.send_keys(Keys.RETURN)
      time.sleep(5)

def openCab():
    try:
        op = driver.find_element_by_link_text("Кабинет")
        op.click()
    
    except Exception:
       print
       
def openUserSetting():
    try:
        usSet = driver.find_element_by_link_text("Настройки участника")
        usSet.click()
        time.sleep(2)
    except Exception:
        print
def openAddress():
    try:
        usAddress = driver.find_element_by_link_text("Адреса")
        usAddress.click()
        time.sleep(2)
    except Exception:
        print
def openbranch():
    try:
        usBranch = driver.find_element_by_link_text("Настройка филиалов")
        usBranch.click()
        time.sleep(2)
    except Exception:
        print

def tendercomission():
    try:
        usTdrComission = driver.find_element_by_link_text("Тендерная комиссия")
        usTdrComission.click()
        time.sleep(2)
    except Exception:
        print

def additionally():
    try:
        usAdd = driver.find_element_by_link_text("Дополнительно")
        usAdd.click()
        time.sleep(2)
    except Exception:
        print

def additionallyEdit():
      try:
         usAdd = driver.find_element_by_link_text("Редактировать")
         usAdd.click()
         time.sleep(2)
         editip = driver.find_element_by_id("comadditional-com_full_name")
         
         editip.clear()
         time.sleep(2)
         editip.send_keys("Leskhan")
         time.sleep(4)
         edit1 = driver.find_element_by_id("comadditional-first_man_fio")
         edit1.clear()
         time.sleep(3)
         edit1.send_keys("Лесхан Каратаев")
         edit1.send_keys(Keys.RETURN)
      except Exception:
         print
#foradding bank rekvizit       
'''def addBankRek():
    try:
        bankrek = driver.find_element_by_link_text("Добавить банковские реквизиты")
        bankrek.click()
        bank = driver.find_element_by_id("select2-combankreq-ref_banks_id-container")
        bank.click()
        time.sleep(2)
        span = self.driver.find_element_by_link_text("АО «KaspiBank»")
        span.click()
    except Exception:
        print
'''
LoginTo()
openCab()
openUserSetting()
openAddress()
openbranch()
tendercomission()
additionally()
additionallyEdit()





