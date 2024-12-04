st1={10,20,30,40,50}

st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)

print(intersection_set)


#union

union_set=st1.union(st2)

print(union_set)

#difference

difference_set=st1.difference(st2)

print(difference_set)


#remove

st1={10,20,60,70,80}

st1.remove(60)

print(st1)
