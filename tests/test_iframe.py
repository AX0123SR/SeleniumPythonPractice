import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

def test_frame():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
    driver.find_element(By.XPATH,"//*[@id='main']/div[2]/div/div[1]/a[1]").click()
    time.sleep(4)