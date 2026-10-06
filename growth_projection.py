initial_revenue = float(input("Enter initial revenue: $"))
growth_rate = float(input("Enter yearly growth rate (%): "))

growth_decimal = growth_rate / 100

revenue = initial_revenue

print("\nProjected Revenue Over 10 Years")
print("-------------------------------")
print(f"{'Year':<6}{'Revenue':>15}")

for year in range(1, 11):
    revenue = revenue * (1 + growth_decimal)
    print(f"{year:<6}${revenue:>14,.2f}")