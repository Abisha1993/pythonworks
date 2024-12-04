#6 list of fruits and prices

fruits=['apple','banana','cherry']

prices=[100,50,250]
  #dictionary comprehension
fruit_prices={fruit: price for fruit, price in zip(fruits,prices)}

print(fruit_prices)