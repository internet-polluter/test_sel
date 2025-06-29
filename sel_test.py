from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Specify the path to your GeckoDriver executable
# If geckodriver is in your system's PATH, you might not need this line
geckodriver_path = '/opt/homebrew/bin/geckodriver' # Replace with the actual path

# Create a Service object for GeckoDriver
service = Service(geckodriver_path)

# Initialize the Firefox driver
driver = webdriver.Firefox(service=service)

try:
    # Go to a website
    driver.get("https://www.google.com") # Replace with the desired URL

    # Print the title of the page to verify
    print(f"Page title: {driver.title}")

    # You can add more interactions here, for example, finding an element:
    # element = driver.find_element(By.TAG_NAME, "h1")
    # print(f"Found element text: {element.text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
