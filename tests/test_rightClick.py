import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


def test_rightClick():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.geeksforgeeks.org/")
    driver.maximize_window()
    data = driver.find_element(By.XPATH,"//a[text()='Data Science']")
    act = ActionChains(driver)
    time.sleep(2)
    # Right click
    act.context_click(data).perform()
    time.sleep(2)

    # Double Click
    # data = driver.find_element(By.XPATH, "//a[text()='Data Science']")
    # act = ActionChains(driver)
    # time.sleep(2)
    # # Right click
    # act.double_click(data).perform()
    # time.sleep(2)
