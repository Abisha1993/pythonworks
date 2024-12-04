def find_common_elements(lists):
    if not lists:
        return[]
    
    common_elements=set(lists[0]).intersection(*lists[1:])
    return list(common_elements)
list_of_lists=[[1,2,3,4],[2,4,6,8],[2,4,10,12]]
common_elements=find_common_elements(list_of_lists)
print("common elements:",common_elements)
