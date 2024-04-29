import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def test_googlesearch(driver):
    googleSearch = driver.find_element(By.ID,"APjFqb")
    googleSearch.send_keys("Automation")
    googleSearch.send_keys(Keys.ENTER)
    time.sleep(2)
    print("Test Completed")