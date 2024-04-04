from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def testAlert():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.implicitly_wait(10)

    prompt_button = driver.find_element(By.XPATH, "//button[text()='Prompt']")
    prompt_button.click()

    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.send_keys("Ayush Srivastava")
        alert.accept()
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        driver.quit()

