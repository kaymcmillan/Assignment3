preferences = ["coffee", "tea", "coffee", "soda"]

counts = {}

for choice in preferences:
    if choice in counts:
        counts[choice] += 1
    else:
        counts[choice] = 1

total_responses = len(preferences)

print("Market Survey Results")
for product, count in counts.items():
    percent = (count / total_responses) * 100
    print(f"{product}: {percent:.0f}%")