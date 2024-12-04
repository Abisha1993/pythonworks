def find_second_largest(num1,num2,num3):
    if (num1>num2 and num1<num3):
        return num1
    elif (num2>num1 and num2<num3):
        return num2
    else:
        return num3
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    num3=float(input("enter the third number:"))
    second_largest=find_second_largest(num1,num2,num3)
    print("the second largest number is:",second_largest)z