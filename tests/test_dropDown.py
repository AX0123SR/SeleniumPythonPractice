import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


def test_dropDown():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
    driver.implicitly_wait(10)

    dropdown = driver.find_element(By.XPATH,"//*[@id='post-2646']/div[2]/div/div/div/p/select")

    drop = Select(dropdown)
    drop.select_by_visible_text("India")
    time.sleep(6)