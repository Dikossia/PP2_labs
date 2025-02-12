import re
import json

with open(r"c:\Users\Huawei\Desktop\PP2_labs\lab_5\row.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Step 1: Extract Store Details
store_pattern = r"Филиал\s+ТОО\s+(.+)"
receipt_pattern = r"Чек №(\d+)"
total_pattern = r"ИТОГО:\s*([\d\s]+,\d{2})"
datetime_pattern = r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})"

store_match = re.search(store_pattern, text)
receipt_match = re.search(receipt_pattern, text)
total_match = re.search(total_pattern, text)
datetime_match = re.search(datetime_pattern, text)

store_name = store_match.group(1) if store_match else "Unknown"
receipt_number = receipt_match.group(1) if receipt_match else "Unknown"
total_amount = total_match.group(1) if total_match else "Unknown"
transaction_time = datetime_match.group(1) if datetime_match else "Unknown"

# Step 2: Extract Purchased Items
item_pattern = r"\d+\.\s*\n(.+?)\n([\d,]+)\s*x\s*([\d,]+)\n([\d,\s]+)"
items = re.findall(item_pattern, text)

item_list = []
for item in items:
    name = item[0].strip()
    quantity = item[1].replace(",", ".")
    price_per_unit = item[2].replace(",", ".")
    total_price = item[3].replace(",", ".").replace(" ", "")

    item_list.append({
        "Name": name,
        "Quantity": float(quantity),
        "Price per unit": float(price_per_unit),
        "Total Price": float(total_price)
    })

# Step 3: Store Data in a JSON File
receipt_data = {
    "Store Name": store_name,
    "Receipt Number": receipt_number,
    "Total Amount": total_amount,
    "Transaction Time": transaction_time,
    "Items": item_list
}

with open("receipt.json", "w", encoding="utf-8") as json_file:
    json.dump(receipt_data, json_file, ensure_ascii=False, indent=4)

# Step 4: Print Extracted Data
print("Store Name:", store_name)
print("Receipt Number:", receipt_number)
print("Total Amount:", total_amount)
print("Transaction Time:", transaction_time)
print("\nPurchased Items:")
for item in item_list:
    print(item)

print("\n✅ Receipt data saved to receipt.json")
