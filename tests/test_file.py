import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def test2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.satisfice.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    alls = driver.find_element(By.XPATH,"//li[@id='menu-item-204']")
    action = ActionChains(driver)
    action.move_to_element(alls).perform()

    all_class=[]
    all_classes = driver.find_elements(By.XPATH,"//li[@id='menu-item-204']/ul/li/a/span")
    # print(len(all_classes))
    for element in all_classes:
        all_class.append(element.text)
    print(all_class)


def test2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.flipkart.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    hover = driver.find_element(By.XPATH,"//img[@class='-dOa_b XdYXbi']")
    action = ActionChains(driver)
    action.move_to_element(hover).perform()
    driver.find_element(By.XPATH,"//span[text()='Login']//following::ul/a[2]/li[text()='My Profile']").click()
    time.sleep(3)