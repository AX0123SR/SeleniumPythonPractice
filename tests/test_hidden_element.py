import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService

def test_hiddenElement():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
    time.sleep(2)
    ele = driver.find_element(By.ID,"myDIV").is_displayed()
    print(ele)
    driver.find_element(By.XPATH,"//button[text()='Toggle Hide and Show']").click()
    ele = driver.find_element(By.ID, "myDIV").is_displayed()
    print(ele)

def test_hiddenElement_yatra():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.yatra.com/hotels")
    time.sleep(2)
    driver.find_element(By.XPATH,"//i[@class='icon icon-angle-right arrowpassengerBox']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[text()='Below 12 years']//following::span[@class='ddSpinnerPlus']").click()
    time.sleep(2)
    isDisplayed = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
    print(isDisplayed)
    dropdown =  driver.find_element(By.XPATH,"//select[@class='ageselect']")
    drop = Select(dropdown)
    drop.select_by_value("9")
    time.sleep(6)