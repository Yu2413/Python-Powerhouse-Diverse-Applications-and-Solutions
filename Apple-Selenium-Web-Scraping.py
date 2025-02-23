from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment if you want to run in headless mode

# Initialize the driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    # Navigate to the Yahoo Finance page for Apple Inc.
    url = "https://finance.yahoo.com/quote/AAPL/?p=AAPL"
    driver.get(url)

    # Wait until the page is fully loaded
    wait = WebDriverWait(driver, 30)  # Increased wait time
    wait.until(EC.title_contains("AAPL"))  # Wait for the page title to contain "AAPL"

    # Wait for the stock price element to be visible
    try:
        price_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="qsp-price"]')))
        stock_price = price_element.text
        print("Apple Inc. stock price:", stock_price)
    except TimeoutException:
        print("Stock price element not found. The page structure might have changed.")

finally:
    # Close the WebDriver
    driver.quit()