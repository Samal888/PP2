import re
import json

# open receipt file
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("----- RECEIPT DATA -----")
print(text)


# 1. Extract prices
prices = re.findall(r"\d+\.\d{2}", text)

print("\nPrices found:")
print(prices)


# 2. Extract product names
products = re.findall(r"([A-Za-z]+)\s\d+\.\d{2}", text)

print("\nProducts found:")
print(products)


# 3. Calculate total
numbers = [float(p) for p in prices]
total = sum(numbers[:-1])   # last price is total already

print("\nCalculated total:", total)


# 4. Extract date
date = re.search(r"\d{4}-\d{2}-\d{2}", text)

if date:
    print("\nDate:", date.group())


# 5. Extract time
time = re.search(r"\d{2}:\d{2}", text)

if time:
    print("Time:", time.group())


# 6. Extract payment method
payment = re.search(r"Payment Method:\s(\w+)", text)

if payment:
    print("Payment Method:", payment.group(1))


# 7. Create structured data (JSON)
data = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date.group() if date else None,
    "time": time.group() if time else None,
    "payment_method": payment.group(1) if payment else None
}

print("\n----- JSON OUTPUT -----")
print(json.dumps(data, indent=4))

print("\n----- REGEX EXAMPLES -----")

text_example = "My phone number is 12345 and 67890"

# re.search
result = re.search(r"\d+", text_example)
print("search:", result.group())

# re.findall
numbers = re.findall(r"\d+", text_example)
print("findall:", numbers)

# re.split
words = re.split(r"\s", text_example)
print("split:", words)

# re.sub
new_text = re.sub(r"\d+", "NUMBER", text_example)
print("sub:", new_text)