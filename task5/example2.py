def max_profit(prices):
    min_price=float('inf')
    max_profit=0
    for price in prices:
        min_price=min(min_price,price)
        profit=price-min_price
        max_profit=max(max_profit,profit)
    return max_profit
prices=[7,6,4,3,1]
print(max_profit(prices))