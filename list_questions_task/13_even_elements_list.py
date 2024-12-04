def find_even_numbers(numbers):
    even_numbers=[]
    for number in numbers:
        if number % 2 ==0:
    even_numbers.append(number)
    return even_numbers
input_list=[1,2,3,4,5,6,7,8,9,10]
even_numbers=find_even_numbers(input_list)
print("even numbers in the list:",even_numbers)

    