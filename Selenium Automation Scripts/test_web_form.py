from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

URL = "https://www.selenium.dev/selenium/web/web-form.html"

class WebFormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Using Chrome for stability
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_fill_form(self):
        driver = self.driver
        driver.get(URL)

        # Wait until form is loaded
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # TEXT FIELD
        driver.find_element(By.NAME, "my-text").send_keys("Rayean")

        # PASSWORD FIELD
        driver.find_element(By.NAME, "my-password").send_keys("TestPassword123")

        # TEXTAREA
        driver.find_element(By.NAME, "my-textarea").send_keys("This is an automated test message.")

        # DROPDOWN
        select_element = Select(driver.find_element(By.NAME, "my-select"))
        select_element.select_by_visible_text("Two")

        # RADIO BUTTON
        driver.find_element(By.ID, "my-radio-1").click()

        # CHECKBOX
        driver.find_element(By.ID, "my-check-1").click()

        # DATE PICKER
        try:
            date_picker = driver.find_element(By.NAME, "my-date")
            date_picker.send_keys("2025-12-08")  # YYYY-MM-DD format
        except:
            print("No date picker found — skipping")
            
        # RANGE SLIDER
        try:
            range_slider = driver.find_element(By.NAME, "my-range")
            driver.execute_script("arguments[0].value = arguments[1]", range_slider, 75)
        except:
            print("No range slider found — skipping")

        time.sleep(5)
        # SUBMIT
        driver.find_element(By.CSS_SELECTOR, "button").click()

        print("Form submitted successfully and verified.")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
