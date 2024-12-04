arr=[10,20,30,40,2,3]

result={}

for num in arr:
    square=num**2
    result[num]=square
    print(result)


    arr=[10,20,30,40,2,3]

    result={num:num**3 for num in arr}

    print(result)

    even_squares={num:num**2 for num in arr if num%2==0}

    print(even_squares)
    odd_cubes={num:num**3 for num in arr if num%2!=0}
    print(odd_cubes)


    arr
