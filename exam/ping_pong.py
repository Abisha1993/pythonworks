
number=int(input("enter an integer:"))

if number % 15 == 0:
    print("PINGPONG")

elif number % 3 ==0:

    print("PING")

elif number % 5 ==0:
    print("PONG")
else:
    print(number)