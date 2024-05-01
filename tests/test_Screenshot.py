import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService

def test_screenshot():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

    continue_btn = driver.find_element(By.ID,"login-continue-btn")
    continue_btn.screenshot(".\\continue.png")
    time.sleep(2)
    continue_btn.click()
    time.sleep(1)
    driver.save_screenshot(".\\error.png")
    time.sleep(2)