lst=[1,2,
    [10,20],
    [1,2,5,[10,3]],
    100]

lst_objects=[item for item in lst if instance(item,lst)]

print(max(lst_objects,key=len)).

