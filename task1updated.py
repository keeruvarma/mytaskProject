import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


WebDriverWait(driver, 20).until(EC.url_contains("inventory"))

print("Login successful")
time.sleep(10)

driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
time.sleep(3)
driver.find_element(By.ID,"about_sidebar_link").click()
time.sleep(10)
logo = driver.find_element(By.XPATH, "(//img[@alt='Saucelabs'])[1]")

if logo.is_displayed():
       print(" logo is present and visible.")
else:
       print(" logo is present but not visible.")

time.sleep(10)

driver.quit()

