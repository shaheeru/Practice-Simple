from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()


#driver.get("https://www.daraz.pk/products/i147480002-s1310692004.html?urlFlag=true&mp=1")
driver.get("https://member.daraz.pk/user/login?spm=a2a0e.home.header.d5.35e34937UaZXg8&redirect=https%3A%2F%2Fwww.daraz.pk%2F")
time.sleep(10)
#action = webdriver.common.action_chains
#driver.find_element_by_link_text("login").click()
#driver.find_element_by_class_name("add-to-cart-buy-now-btn").click()
#time.sleep(30)
driver.implicitly_wait(30)
#element = WebDriverWait(driver,20).until(
#EC.presence_of_element_located((By.CLASS_NAME, "mod-input-password-icon"))
 #)
#obj = driver.switch_to.alert()  #.dismiss()
#obj.dismiss()
#driver.find_element_by_xpath("//button[@class='airship-btn-deny']").click()
#driver.find_element_by_xpath("//input[@type='text']").send_keys("darazqa@gmail.com")
#driver.find_element_by_id('q').send_keys("test")
driver.find_element_by_xpath("//input[@placeholder='Please enter your Phone Number or Email']").send_keys("darazqa@gmail.com")
driver.find_element_by_xpath("//input[@placeholder='Please enter your password']").send_keys("Test@123")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(10)
driver.find_element_by_id('q').send_keys("test")
#driver.find_element_by_class_name('search-box__button--1oH').click()
driver.find_element_by_xpath("//button[@class='search-box__button--1oH7']").click()
time.sleep(5)
driver.find_element_by_xpath("//img[@alt='Test Strips - Pack of 10']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[@class='pdp-button-text']").click()
time.sleep(5)
driver.find_element_by_xpath("//button[@class='next-btn next-btn-primary next-btn-large checkout-order-total-button']").click()
time.sleep(10)
driver.find_element_by_id('automation-payment-method-item-103').click()
time.sleep(3)
driver.find_element_by_id('creditCard').send_keys('123456')
time.sleep(3)
driver.find_element_by_xpath("//input[@id='expiryDate']").click()

errormsg = driver.find_element_by_xpath("//div[@class='next-form-item-explain']").text
print(errormsg)

#driver.find_element_by_class_name("airship-btn-deny").click()
#a2a0e.searchlist.list.i40.49ef120abCN4yu
#pdp-button-text
#c1ZEkM
#add-to-cart-buy-now-btn  pdp-button pdp-button_type_text pdp-button_theme_bluedaraz pdp-button_size_xl