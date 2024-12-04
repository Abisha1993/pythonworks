#10 dictionary comprehension 
prices={'apple':100,"banana":50,'cherry':200,'date':80,'orange':150}

discounted_prices={item:price * 0.9 for item,price in prices.items()}
print("original prices:")
print(prices)
print("\nDiscounted prices:")
print(discounted_prices)
