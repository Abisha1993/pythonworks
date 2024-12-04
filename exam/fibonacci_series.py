def next_fibonacci_number(number: int)-> int:
    a,b=0,1
    while b<= number:
        a,b=b,a+b
        return b
    