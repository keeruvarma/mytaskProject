import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.current_url)

driver.find_element(By.NAME, "user-name").send_keys(": locked_out_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").click()
message = driver.find_element(By.XPATH,"//div[@class='error-message-container error']").text
print(message)

time.sleep(10)




