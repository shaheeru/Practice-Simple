from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.LoginPage import LoginPage
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        #driver.close()
        #driver.quit()
        print("Completed")

    def test_login(self,test_setup):
        driver.get(LoginPage.AdminLoginURL)
        #element = WebDriverWait(driver,20).until(
         #   EC.presence_of_element_located((By.CLASS_NAME, "airship-alert-logo"))
        #)
        #driver.find_element_by_css_selector('button.airship-btn').click()
        #driver.find_element_by_xpath("//button[@class='airship-btn-deny']").click()
        #driver.find_element_by_tag_name('button').click()
        #driver.find_element_by_link_text("Not Interested").click
        #driver.find_element_by_link_text("login").click()
        driver.find_element_by_id(LoginPage.emailField).send_keys("qa@voicevoice.com")
        driver.find_element_by_id(LoginPage.passwordField).send_keys("vApp~1732")
        x = driver.title
        assert x == "VoiceVoice"
        driver.find_element_by_class_name(LoginPage.googleButton).click()

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Completed")