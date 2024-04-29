import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


def test_Calendar():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
    monthYear = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']").text
    month = monthYear.split(" ")[0]
    year = monthYear.split(" ")[1]
    print(month)
    print(year)
    while not ((month == "December") & (year == "2025")):
        driver.find_element(By.XPATH,"//span[text()='Next']").click()
        monthYear = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']").text
        month = monthYear.split(" ")[0]
        year = monthYear.split(" ")[1]
    time.sleep(4)
    driver.find_element(By.XPATH,"//a[text()='19']").click()
    time.sleep(4)


    # all_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")
    # for i in all_dates:
    #     data = i.text
    #     print(data)
    #     if data == "25":
    #         i.click()
    #         break
    # time.sleep(4)