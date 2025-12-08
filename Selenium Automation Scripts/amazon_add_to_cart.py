from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://www.amazon.com/")

# Wait for search box and search for "laptop"
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)
search_box.send_keys("samsung galaxy s25 ultra")

# Click search button
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
)
search_button.click()

# Wait for the first product image and click first image
first_image = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "img.s-image"))
)
first_image.click()

# Wait and click the Add to Cart button
cart_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
)
cart_button.click()

# Wait a few seconds before closing the browser
time.sleep(10) 

# Close the browser
driver.quit()

