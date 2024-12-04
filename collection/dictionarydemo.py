product={"id":1000,"tittle":"goodday","price":35,"brand":"britania"}

print(product["price"])


#produt update

product["brand"]="parle"

print(product)

product["use by date"]="12-10-2024"

print(product)



product["offer"]=5

print(product)


#add offer as 10 if offer not exist else add offer

if "offer"in product:
    product["offer"]=10
else:
    product["offer"]=20

    print(product)