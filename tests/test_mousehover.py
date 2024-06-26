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
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    more_button = driver.find_element(By.XPATH,"//span[@class='more-arr']")
    action = ActionChains(driver)
    action.move_to_element(more_button).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[@title='Adventures']").click()
    time.sleep(2)


    # driver.implicitly_wait(10)
    # home = driver.find_element(By.XPATH,"//a[text()='Home']")
    # act = ActionChains(driver)
    # act.move_to_element(home).perform()
    # time.sleep(4)