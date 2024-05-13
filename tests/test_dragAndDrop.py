import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


def test_dragAndDrop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   # driver.get("https://demo.guru99.com/test/drag_drop.html")
    driver.get("https://jqueryui.com/droppable/")
    driver.maximize_window()
    # driver.switch_to.frame("//*[@id='post-2669']/div[2]/div/div/div[1]/p/iframe")
    # src = driver.find_element(By.XPATH,"//*[@id='fourth']/a")
    # dest = driver.find_element(By.XPATH,"//*[@id='amt7']/li")
    # act = ActionChains(driver)
    # act.drag_and_drop(src, dest).perform()

    driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
    src = driver.find_element(By.ID,"draggable")
    dest = driver.find_element(By.ID,"droppable")
    act = ActionChains(driver)
    #act.drag_and_drop(src, dest).perform()
    # drag and drop at some co-ordinates
    act.drag_and_drop_by_offset(src,50,70).perform()
    time.sleep(3)
