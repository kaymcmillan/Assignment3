sales = {"Alice": 5000, "Bob": 7000, "Carol": 4000}


def calculate_commission(sale_amount):
    """Return a 10% commission on a sale amount."""
    return sale_amount * 0.10


results = []
for name, amount in sales.items():
    commission = calculate_commission(amount)
    results.append((commission, name))

results.sort(reverse=True)

print("Commission Leaderboard:")
print("----------------------")
rank = 1
for commission, name in results:
    print(f"{rank}. {name}: ${commission:,.2f}")
    rank += 1