import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

def test_cookie():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
    language = driver.find_element(By.ID,"langSelect-EN")
    language.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    cookie = driver.find_element(By.ID,"bigCookie")
    cookie.click()

    time.sleep(6)