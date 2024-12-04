#def add_numbers(*args):

    #print(args)
#add_numbers(10,20)
#add_numbers(10,20,30)


#def product(*args):
    #result=1
    #for num in args:
       # result=result*num
        #return result
    #print(product(10,20,5,6))

# create afunction that accept any number of arguments and return second maximum number
def second_max_number(*args):
    sorted_numbers=sorted(args,reverse=True)
    return sorted_numbers[1]
    print(second_max_number(10,11,12,13))

    