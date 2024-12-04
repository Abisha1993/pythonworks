def split_list(input_list):
    mid_index=len(input_list)//2
    first_half=input_list[:mid_index]
    second_half=input_list[mid_index:]
    return first_half,second_half
if __name__ =="__main__":
    my_list=[1,2,3,4,5,6,7]
    first_half,second_half=split_list(my_list)
    print("first half:",first_half)
    print("second half:",second_half)