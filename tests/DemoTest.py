import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.imdb.com/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//span[text()='Menu']").click()
driver.find_element(By.XPATH,"//span[text()='Top 250 Movies']").click()
time.sleep(4)


all_elements = driver.find_elements(By.XPATH,"//h3[@class='ipc-title__text']")
print(len(all_elements))
for i in all_elements:
    print(i.text)
