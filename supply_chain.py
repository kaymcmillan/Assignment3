warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]

totals = {}

for warehouse in warehouses:
    for product, quantity in warehouse["inventory"].items():
        if product in totals:
            totals[product] += quantity
        else:
            totals[product] = quantity

print("Total Stock Across Supply Chain")
print("-------------------------------")
for product, total in totals.items():
    print(f"{product}: {total}")