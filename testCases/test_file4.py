import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

import time

from selenium.webdriver.common.by import By


class TestClass4:

    @pytest.mark.CredKart
    @pytest.mark.web
    @pytest.mark.skip
    def test_Credkart_Register007(self):

        # 1 Open browser
        driver = webdriver.Chrome(options=chrome_options)

        # 2 Go to URL "https://automation.credence.in/"
        driver.get("https://automation.credence.in/register")

        # 3 Enter Name
        driver.find_element(By.ID, "name").send_keys("Python automation")

        # 4 Enter Email Id
        driver.find_element(By.ID, "email").send_keys("2may2024@gmail.com")

        # 5 Enter Password
        driver.find_element(By.ID, "password").send_keys("Test@123")

        # 6 Enter Confirm Password
        driver.find_element(By.ID, "password-confirm").send_keys("Test@123")

        time.sleep(3)
        # 7 Click on Register button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # 8 Verify Registration
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Registration test cases pass")
            assert True
        except:
            print("Registration test cases fail")
            assert False

        # 9 quit the driver
        driver.quit()

        # selectorhub
        # test case studio

    @pytest.mark.web

    def test_Credkart_URL008(self):
        # 1 Open browser
        driver = webdriver.Chrome(options=chrome_options)
        # 2 Go to URL "https://automation.credence.in/"

        driver.get("https://automation.credence.in/")

        # 3 Verify URL
        if driver.title == "CredKart":
            print(driver.title)
            print("Credkart url test case pass")
            assert True
        else:
            print("Credkart url test case fail")
            assert False

        driver.quit()
