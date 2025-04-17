from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

# 1. Setup Chrome options to disable password manager popup
options = webdriver.ChromeOptions()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

# 2. Open the website
driver.get("https://www.saucedemo.com")
driver.maximize_window()

# 3. Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# 4. Sort by "Price (high to low)"
sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
sort_dropdown.select_by_visible_text("Price (high to low)")

# 5. Add the highest-priced product (first one after sorting)
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item"))
)
driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

# 6. Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# 7. Checkout
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
).click()

# 8. Enter user details
driver.find_element(By.ID, "first-name").send_keys("Alice")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("592")
driver.find_element(By.ID, "continue").click()

# 9. Verify total amount is $49.99
total_amount = driver.find_element(By.CLASS_NAME, "summary_total_label").text
assert "$49.99" in total_amount, f"Expected $49.99 but got {total_amount}"

# 10. Finish checkout
driver.find_element(By.ID, "finish").click()

# 11. Verify thank you message
thank_you = driver.find_element(By.CLASS_NAME, "complete-header").text
assert thank_you == "Thank you for your order!", "Checkout did not complete as expected."

print("Test completed successfully.")

# Close browser
driver.quit()
