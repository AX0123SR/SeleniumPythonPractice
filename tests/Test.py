import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.google.com")
#
# time.sleep(2)
# googleSearch = driver.find_element(By.ID,"APjFqb")
# googleSearch.send_keys("Automation")
# googleSearch.send_keys(Keys.ENTER)

driver.get("https://trytestingthis.netlify.app/")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

time.sleep(2)
driver.quit()
