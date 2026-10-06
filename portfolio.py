# Exercise 5: Stock Portfolio Tracker
import random

# Each stock has a number of shares and a price per share
portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}


def calculate_total(portfolio):
    """Add up shares * price for every stock and return the total."""
    total = 0
    for stock, info in portfolio.items():
        total += info["shares"] * info["price"]
    return total


print("Portfolio Summary")
print("-----------------")
for stock, info in portfolio.items():
    value = info["shares"] * info["price"]
    print(f"{stock}: {info['shares']} shares x ${info['price']:,.2f} = ${value:,.2f}")

print("-----------------")
print(f"Total value: ${calculate_total(portfolio):,.2f}")

print("\nOne-Week Simulation")
print("-------------------")
for day in range(1, 8):
    # Nested loop: change the price of every stock for this day
    for stock, info in portfolio.items():
        change = random.uniform(-0.05, 0.05)   # a random number between -5% and +5%
        info["price"] = info["price"] * (1 + change)

    print(f"Day {day}: total value = ${calculate_total(portfolio):,.2f}")