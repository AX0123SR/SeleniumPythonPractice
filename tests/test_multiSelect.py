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
    driver.get("https://pynishant.github.io/dropdown-selenium-python-select.html")
    dropdown = driver.find_element(By.ID,"lang2")
    drop = Select(dropdown)
    drop.select_by_visible_text("PHP")
    drop.select_by_value("python")
    drop.select_by_index(3)
    time.sleep(3)
    drop.deselect_by_visible_text("PHP")
    time.sleep(3)