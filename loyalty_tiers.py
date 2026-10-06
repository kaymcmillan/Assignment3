customers = {
    "Patrick": 800,
    "Sarah": 2500,
    "Paul": 6000,
    "Matt": 1000,
    "Kaylie": 4999,
    "Nick": 12000
}

tier_counts = {"Bronze": 0, "Silver": 0, "Gold": 0}

print("Customer Tiers")
print("--------------")

for name, total_purchases in customers.items():
    if total_purchases >= 5000:
        tier = "Gold"
    elif total_purchases >= 1000:
        tier = "Silver"
    else:
        tier = "Bronze"

    tier_counts[tier] += 1
    print(f"{name}: ${total_purchases:,.2f} -> {tier}")

print("\nTier Summary")
print("------------")
for tier, count in tier_counts.items():
    print(f"{tier}: {count} customers")