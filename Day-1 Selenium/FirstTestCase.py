#Open URL-https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index
#Enter username -Admin
#enter password -admin123
#click on login
#Capture title of home page.(Actual title)
#Verify title of home page OrangeHRM(Expected)
#Close Browser


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keep the browser open after execution

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

try:
    # Wait for the username field to be present and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("Admin")

    # Wait for the password field to be present and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys("admin123")

    # Find and click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

    # Wait for an element on the dashboard page to verify login success
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h6"))  # Adjust selector based on the actual element
    )

    # Print the actual title to debug
    act_title = driver.title
    print(f"Actual title after login: {act_title}")

    exp_title = "OrangeHRM"  # Expected title
    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login Test Failed")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after a delay
    input("Press Enter to close the browser...")  # Wait for user input before closing
    driver.quit()
