#1  access andprint the age of one person using their name

people={"john":25,"vicky":34,"micheal":40,"sophia":28,"william":35}

name="vicky"
age=people.get(name)
if age:
    print(f"{name} is {age} years old.")
else:
    print(f"none")