import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()



# 1. Find prices (формат 154,00 или 1 200,00)
prices = re.findall(r"\d[\d\s]*,\d{2}", text)

print("\nPrices:")
print(prices)

# 2. Find product names (строки перед количеством)
products = re.findall(r"\d+\.\n([^\n]+)", text)

print("\nProducts:")
print(products)

# 3. Find payment method
payment = re.search(r"Банковская карта", text)

if payment:
    payment_method = "Card"
else:
    payment_method = "Unknown"

print("\nPayment Method:", payment_method)

# 4. Find date and time
datetime = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)

if datetime:
    print("\nDate and Time:", datetime.group())

# 5. Create JSON output
data = {
    "products": products,
    "prices": prices,
    "payment_method": payment_method,
    "datetime": datetime.group() if datetime else None
}

print("\n----- JSON OUTPUT -----")
print(json.dumps(data, indent=4, ensure_ascii=False))