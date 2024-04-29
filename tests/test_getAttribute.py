import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def test_getAttributeValue():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.yatra.com/")
    time.sleep(2)
    getat = driver.find_element(By.ID,"BE_flight_flsearch_btn").get_attribute("class")
    print(getat)