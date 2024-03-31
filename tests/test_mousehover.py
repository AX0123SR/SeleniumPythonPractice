import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


def test_mouseHover():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demo.guru99.com/test/newtours/index.php")
    driver.implicitly_wait(10)
    home = driver.find_element(By.XPATH,"//a[text()='Home']")
    act = ActionChains(driver)
    act.move_to_element(home).perform()
    time.sleep(4)