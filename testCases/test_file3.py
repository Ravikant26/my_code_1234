import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


class TestClass3:

    @pytest.mark.regression
    @pytest.mark.web
    def test_Credence005(self):
        driver = webdriver.Chrome(options=chrome_options)
        #driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        try:
            driver.find_element(By.XPATH, "//img[@alt='Credence IT']")
            assert True
        except:
            assert False
        driver.quit()

    @pytest.mark.web
    @pytest.mark.regression
    def test_Credkart_Login006(self):

        # 1 Open browser
        driver = webdriver.Chrome(options=chrome_options)

        # 2 Go to URL "https://automation.credence.in/login"
        driver.get("https://automation.credence.in/login")

        # Enter email
        # XPATH--> XPATH(XML Path Language) is used language to select elements
        # or attribute from HTML pages
        # XPATH Format --> //tagname[@attribute='value']
        # Email Xpath --> //input[@type='email']
        # To check Xpath in browser console --> $x("Xpath")

        # 3 Enter Email Id
        driver.find_element(By.ID, "email").send_keys("2may2024@gmail.com")

        # Enter Password
        # CSS--> CSS(Cascading style sheets) is language used to describe
        # presentation of HTML pages.
        # CSS define visual properties of element like front, front size, colour, layout
        # CSS format --> tagname[attribute='value']
        # password css --> input[id='password']
        # To check CSS in browser console --> $$("CSS")

        # 4 Enter Password
        driver.find_element(By.ID, "password").send_keys("Test@123")

        time.sleep(3)
        # 5 Click on Login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # 6 Verify Login
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login test cases pass")
            assert True
        except:
            print("Login test cases fail")
            assert False

        # 9 quit the driver
        driver.quit()
