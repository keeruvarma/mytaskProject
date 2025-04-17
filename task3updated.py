

import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

dropdown_element = driver.find_element(By.CLASS_NAME,"product_sort_container")
time.sleep(5)

dropdown = Select(dropdown_element)

dropdown.select_by_visible_text("Price (high to low)")
driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").click()
driver.find_element(By.ID,"checkout").click()


driver.find_element(By.ID, "first-name").send_keys("Alice")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("592")
time.sleep(5)
driver.find_element(By.ID, "continue").click()

total_amount = driver.find_element(By.XPATH,"//div[@class='summary_subtotal_label']").text
print("total price:",total_amount)
assert "$49.99" in total_amount


driver.find_element(By.ID, "finish").click()
message = driver.find_element(By.XPATH,"//h2[@class='complete-header']")
print(message.text)
assert "Thank you for your order!" in message.text

driver.quit()
