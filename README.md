# 🛒 E-commerce Test Automation

This repository contains automated UI test scripts for a fictional eCommerce website using **Selenium WebDriver** and **Python**, following the **Page Object Model** design pattern.  
The tests simulate real-world user interactions like logging in, adding items to the cart, and completing the checkout process.

---

## 📌 Technologies Used

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- HTML Test Reports (`pytest-html`)

---

## ✅ Test Overview

### 🔐 `test_login.py` — Login Test
**Description:** Verifies login functionality using valid credentials.  
**Steps:**
1. Navigate to the login page.
2. Enter valid username: `standard_user` and password: `secret_sauce`.
3. Confirm successful redirection to the homepage.

✅ **Pass Criteria:** The homepage is displayed after login.

---

### 🛒 `test_cart.py` — Cart Functionality Test
**Description:** Validates adding items to the cart and checking their presence.  
**Steps:**
1. Log in to the website.
2. Add a product (e.g., "Sauce Labs Backpack") to the cart.
3. Verify that:
   - The cart badge shows the correct quantity.
   - The product is listed in the cart.

✅ **Pass Criteria:** Product appears correctly in the cart with accurate quantity.

---

### 💳 `test_checkout.py` — Checkout Process Test
**Description:** Simulates the full checkout flow from cart review to order completion.  
**Steps:**
1. Add products to the cart.
2. Click “Checkout”.
3. Fill in customer information (first name, last name, zip code).
4. Proceed through the checkout overview.
5. Confirm the order.

✅ **Pass Criteria:** Order confirmation page is displayed after checkout.

---

## 📁 Project Structure

