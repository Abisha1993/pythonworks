#5 lists of keys and values

keys=['apple','banana','cherry']
values=['red','yellow','pink']
   #dictionary comprehension
fruit_colors = {key: value for key, value in zip(keys,values)}
print(fruit_colors)