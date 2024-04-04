import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

def test_frame():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demo.guru99.com/test/guru99home/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.switch_to.frame(driver.find_element(By.ID,'a077aa5e'))
    driver.find_element(By.XPATH,"//img[@src='Jmeter720.png']").click()
    time.sleep(4)