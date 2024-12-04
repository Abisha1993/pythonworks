def find_max_min(lst):
    if len(lst)==0:
        return None, None
    max_val=lst[0]
    min_val=lst[0]
    for num in lst:
        if num> max_val:
            max_val=num
        if num< min_val:
            min_val=num
    return max_val,min_val
numbers=[23,1,56,78,9,12,100,4]
maximum,minimum=find_max_min(numbers)
print("maximum:",maximum)
print("minimum:",minimum)