import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService


def test_keyboardAction():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.lambdatest.com/")
    driver.implicitly_wait(10)
    ele = driver.find_element(By.XPATH,"//a[text()='Get Started Free']")
    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).click(ele).key_up(Keys.CONTROL).perform()
    child_window = driver.window_handles[1]
    driver.switch_to.window(child_window)
    print("\nChild window title: ",driver.title)
    time.sleep(4)