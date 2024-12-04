def merge_and_sort(list1,list2):
    merged_list=list1 + list2
    merged_list.sort()
    return merged_list
list1=[5,2,9,1]
list2=[8,3,7,4]
result=merge_and_sort(list1,list2)
print("merged and sorted list:",result)
