#  E-commerce Budget Match Project

A simple Python project that helps customers find **two products whose combined price equals (or matches)** their available **budget**.  
This simulates a basic **discount or recommendation system** commonly used in e-commerce websites.

---

##  Project Overview

**Goal:**  
Given a list of product prices and a customer's budget, find two products that together cost exactly (or closest to) that budget.

**Example Use Case:**  
A customer has ₹1000 to spend → the system recommends two products that total ₹1000.

---

##  Features

✅ Find two products whose total price equals the customer's budget  
✅ Simple and efficient logic using a **hash map (dictionary)**  
✅ Works with any product-price list  
✅ Can be expanded into a recommendation system or web app later  

---

##  How It Works

### Input:
- Product IDs and Prices  
- Customer’s budget amount

### Output:
- IDs (and prices) of two products that add up to the target budget

---

##  Example

```python
products = {
    101: 250,
    102: 750,
    103: 500,
    104: 300,
    105: 700
}
budget = 1000
