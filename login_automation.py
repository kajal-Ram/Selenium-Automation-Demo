from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver (ensure chromedriver.exe is in the same folder)
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open demo login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait for page to load
time.sleep(2)

# Enter username and password
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# Click on Login button
driver.find_element(By.ID, "submit").click()

# Wait to view result
time.sleep(2)

# Verify login success message
try:
    message = driver.find_element(By.XPATH, "//h1[contains(text(),'Logged In Successfully')]")
    if message.is_displayed():
        print("✅ Login Test Passed: Successfully logged in!")
except Exception as e:
    print("❌ Login Test Failed:", e)

# Wait a bit before closing browser
time.sleep(3)
driver.quit()
