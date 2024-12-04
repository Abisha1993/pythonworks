
def multiply_elements(input_list):
    product=1
    for element in input_list:
        product *= element
        return product
    my_list=[2,3,4]
    result=multiply_elements(my_list)
    print("the product of all elements in the list is:",result)
    