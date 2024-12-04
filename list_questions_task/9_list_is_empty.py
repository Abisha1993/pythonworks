def is_list_empty(my_list):
    if not my_list:
        return True
    return False

my_list=[]

if is_list_empty(my_list):
    print("the list is empty.")
else:
    print("the list is not empty.")