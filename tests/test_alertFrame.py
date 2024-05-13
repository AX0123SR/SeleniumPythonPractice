import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def testAlertFrame():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
    driver.maximize_window()
    driver.switch_to.frame("iframeResult")

    driver.find_element(By.XPATH,"/html/body/button").click()
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.send_keys("Mr Xoxo")
    driver.switch_to.alert.accept()
    time.sleep(2)


