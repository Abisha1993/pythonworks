def collections import counter
my_list=[1,2,2,3,4,4,4,5]
element_count=counter(my_list)
for element,count in element_count.items():
    print(f"element {element}occurs {count} time(s)")