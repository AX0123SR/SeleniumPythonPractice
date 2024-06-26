import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService

def test_checkbox():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.yatra.com/")
    time.sleep(2)
    checkboxes = driver.find_elements(By.XPATH,"//i[@class='ico ico-checkbox']")
    print(len(checkboxes))
    l = ["Student Fare Offer","Non Stop Flights","Armed Forces Offer","Senior Citizen Offer"]
    for i in range(1,len(l)):
        if i!=2:
            driver.find_element(By.XPATH,f"//a[@title='{l[i]}']").click()
            time.sleep(2)
        else:
            continue