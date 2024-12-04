def remove_element_by_index(lst,index):
     if index < 0 or index >= len(lst):
        return "index out of range"
     else:
        lst.pop(index)
        return lst
     my_list=[10,20,30,40,50]
     index_to_remove=2
     result=remove_element_by_index(my_list,index_to_remove)
     print("updated list:",result)