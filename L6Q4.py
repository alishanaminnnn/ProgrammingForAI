# Initial stock dictionary
stock = {"rice": 50, "sugar": 20, "flour": 35, "oil": 10}

# List of daily transactions
transactions = [
    ("sale", "rice", 12),
    ("purchase", "sugar", 15),
    ("sale", "oil", 12),
    ("sale", "flour", 5),
    ("purchase", "tea", 25),
    ("sale", "sugar", 30),
    ("sale", "rice", 20),
    ("sale", "salt", 3)
]

rejected = []
total_sold = 0

# Process transactions in order
for transaction in transactions:
    type, item, quantity = transaction

    if type == "purchase":
        stock[item] = stock.get(item, 0) + quantity

    elif type == "sale":
        if item in stock and stock[item] >= quantity:
            stock[item] -= quantity
            total_sold += quantity
        else:
            rejected.append(transaction)

# Print final stock
print("Final Stock:", stock)

# Print rejected transactions
print("Rejected Transactions:", rejected)

# Print total units sold
print("Total Units Sold:", total_sold)

# Find items with fewer than 10 units left
reorder = sorted([item for item in stock if stock[item] < 10])
print("Items to Reorder:", reorder)
