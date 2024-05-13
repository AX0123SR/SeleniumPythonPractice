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
    driver.get("https://www.snapdeal.com/search?keyword=mobile%20phone&sort=rlvncy")
    driver.maximize_window()
    elem1 = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
    elem2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")

    # 1st way
    #ActionChains(driver).drag_and_drop_by_offset(elem1,60,0).perform()
    # 2nd way
    #ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(50,0).release().perform()
    # 3rd way
    #ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold().move_by_offset(70,0).release().perform()

    ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 0).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop_by_offset(elem2, -70, 0).perform()
    time.sleep(3)
