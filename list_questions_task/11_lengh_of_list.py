def find_length(my_list):
    count=0
    for item in my_list:
        count +=1
        return count
    my_list=[1,2,3,4,5]
    length=find_length(my_list)
    print(f"the length of the list is: {length}")
    