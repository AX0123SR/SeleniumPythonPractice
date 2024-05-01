import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService

def test_autoSuggestion():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    depart_city = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
    depart_city.click()
    time.sleep(2)
    depart_city.send_keys("New Delhi")
    time.sleep(2)
    depart_city.send_keys(Keys.ENTER)
    time.sleep(2)
    arrival_city = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
    arrival_city.click()
    time.sleep(2)
    arrival_city.send_keys("New")
    time.sleep(2)
    search_list = driver.find_elements(By.XPATH,"//div[@class='viewport']/div/div/li")
    print(len(search_list))
    for search in search_list:
        print(search.text)
        if "New Orleans (MSY)" in search.text:
            time.sleep(2)
            search.click()
            break

    driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
    time.sleep(4)
    all_dates = driver.find_elements(By.XPATH,"//table[@class='days-head day-container-table']/tbody/tr/td[@class!='inActiveTD']")
    for date in all_dates:
        if date.get_attribute("data-date") == "12/01/2025":
            date.click()
            time.sleep(4)
            break

    driver.find_element(By.XPATH,"//input[@value='Search Flights']").click()
    time.sleep(3)