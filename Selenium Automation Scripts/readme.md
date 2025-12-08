# 💻 Selenium Scripts

This folder includes **Selenium automation scripts** designed to perform web tasks, such as:

- Searching for products, interacting with items, and adding them to the cart on platforms like Amazon.  
- Filling out and submitting web forms, including text fields, dropdowns, radio buttons, checkboxes, date picker, and range slider using a demo web form.

The scripts showcase **Python-based web automation using Selenium**.

---
## 🚀 Running the Scripts

### **1. Amazon Add to Cart Script**

```bash
python amazon_add_to_cart.py

```
The script will:

   - Open Amazon in a browser
   - Search for a product (e.g., "laptop")
   - Click the first product image
   - Click "Add to Cart"
   - Wait a few seconds before closing the browser
     
### 2. Web Form Automation Script

```bash
python test_web_form.py

```
The script will:

- Open a stable Selenium demo web form in a browser
- Fill out text, password, and textarea fields
- Select dropdown options and click radio buttons / checkboxes
- Interact with advanced inputs: date picker, range slider
- Wait a few seconds before clicking the submit button
- Verify the success message after submission

---

## ⚙️ Features

**Amazon Script (`amazon_add_to_cart.py`)**

- Automated Amazon product search
- Click on product images
- Add products to cart
- Handles dynamic page elements with explicit waits

**Web Form Script (`test_web_form.py`)**

- Fill text, password, and textarea fields automatically
- Select dropdown options
- Click radio buttons and checkboxes
- Interact with date picker, and range slider
- Explicit waits for element visibility and clickable actions
- Verifies successful form submission

---

## 📌 Requirements

- Python 3.8 or later
- Selenium (`pip install selenium`)
- WebDriver for your browser (ChromeDriver / GeckoDriver)

