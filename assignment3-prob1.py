prices = []

print("Enter the price of each item. Enter 0 when you are done.")

while True:
    try:
        price = float(input("Item price: $"))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if price < 0:
        print("Price can't be negative. Try again.")
    elif price == 0:
        break
    else:
        prices.append(price)

if len(prices) > 0:
    total = sum(prices)
    average = total / len(prices)

    print("\n--- Checkout Summary ---")
    print(f"Number of items bought: {len(prices)}")
    print(f"Total purchase amount: ${total:,.2f}")
    print(f"Average item cost: ${average:,.2f}")
else:
    print("No items were entered.")