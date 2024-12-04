def remove_duplicates(input_list):
    return list(set(input_list))
my_list=[1,2,2,3,4,4,5]
new_list=remove_duplicates(my_list)
print(new_list)