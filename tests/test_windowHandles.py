import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

def test_window():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[1]").click()
    parent = driver.current_window_handle
    print("Current window: " + parent)
    child_windows = driver.window_handles
    print(type(child_windows))

    for i in child_windows:
        print(i)
        if i!= parent:
            driver.switch_to.window(i)
            print("\n" + driver.title)
    driver.close()
    driver.switch_to.window(parent)
    print("\n" + driver.title)

    driver.quit()
