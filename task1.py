import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
#print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

alert.accept()

driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.ID,"logout_sidebar_link").click()
logo = driver.find_element(By.XPATH, "(//img[@alt='Saucelabs'])[1]")

if logo.is_displayed():
       print(" logo is present and visible.")
else:
       print(" logo is present but not visible.")

time.sleep(20)



