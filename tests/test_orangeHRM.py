import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_orange():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
    driver.find_element(By.XPATH,"//a[text()='Logout']").click()
    time.sleep(4)
    print(driver.title)