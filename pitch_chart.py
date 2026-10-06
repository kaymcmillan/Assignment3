revenues = [50000, 80000, 120000, 170000, 250000]

dollars_per_symbol = 10000

print("Projected Revenue by Year")
print("(each # = $10,000)")
print("-------------------------")

for i in range(len(revenues)):
    year = i + 1
    bar = "#" * (revenues[i] // dollars_per_symbol)
    print(f"Year {year}: {bar}  ${revenues[i]:,}")

print("\nSame Chart Using a Nested Loop")
print("------------------------------")

for i in range(len(revenues)):
    year = i + 1
    bar = ""
    # Inner loop: add one # at a time
    for symbol in range(revenues[i] // dollars_per_symbol):
        bar += "#"
    print(f"Year {year}: {bar}")