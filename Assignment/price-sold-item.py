# Store prices in a Tuple
prices = tuple(map(float, input("Enter prices of sold items (space-separated): ").split()))

print("\nPrices Tuple:", prices)

# a) Total number of items sold
print("\na) Total number of items sold:", len(prices))

# b) Cheapest item price
print("b) Price of cheapest item: Rs.", min(prices))

# c) Costliest item price
print("c) Price of costliest item: Rs.", max(prices))

# d) Price list in ascending order
sorted_prices = tuple(sorted(prices))
print("d) Price list in ascending order:", sorted_prices)

# e) Number of costliest items sold
costliest = max(prices)
count = prices.count(costliest)
print(f"e) Number of costliest items (Rs. {costliest}) sold: {count}")