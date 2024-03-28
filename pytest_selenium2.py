import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password",[
    ("test","test"),
    ("user","user1"),
    ("t1","t2")
])

def test_login(driver,username,password):
    driver.get("https://trytestingthis.netlify.app/")
    user_name = driver.find_element(By.ID,"uname")
    pass_word = driver.find_element(By.ID,"pwd")
    submit = driver.find_element(By.XPATH,"//input[@type='submit']")

    user_name.send_keys(username)
    pass_word.send_keys(password)
    submit.click()
    assert "Successful" in driver.page_source

