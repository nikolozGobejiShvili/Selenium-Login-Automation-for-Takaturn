from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Setup WebDriver
service = Service(r'C:\Users\Greench Pc\Desktop\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the Takaturn login page
    driver.get("https://takaturn.io/login")

    # Writing the login test case
    def test_login(username, password):
        try:
            # Locate the username and password fields and the login button
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
            username_field = driver.find_element(By.ID, "email")
            password_field = driver.find_element(By.ID, "password")
            login_button = driver.find_element(By.ID, "login-btn")

            # Clear the fields
            username_field.clear()
            password_field.clear()

            # Enter login information
            username_field.send_keys(username)
            password_field.send_keys(password)
            
            # Click the login button
            login_button.click()
            
            # Check for successful login, e.g., by verifying the URL or looking for a logout button
            WebDriverWait(driver, 10).until(
                lambda d: "dashboard" in d.current_url or d.find_element(By.ID, "logout_button")
            )

        except NoSuchElementException as e:
            print("An element was not found:", e)

    # Call your test function with credentials
    test_login("your_username", "your_password")

finally:
    # Close the browser after testing
    driver.quit()
