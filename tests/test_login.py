import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_username("test")
    time.sleep(1)
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_login()
    time.sleep(2)

    #
    #
    # driver.get("https://trytestingthis.netlify.app/")
    # user_name = driver.find_element(By.ID,"uname")
    # pass_word = driver.find_element(By.ID,"pwd")
    # submit = driver.find_element(By.XPATH,"//input[@type='submit']")
    #
    # user_name.send_keys("test")
    # pass_word.send_keys("test")
    # submit.click()
    assert "Successful" in driver.page_source

