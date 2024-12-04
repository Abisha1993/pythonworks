lst

st=set()

st={10,20,30}

print(st)


st1={1,2,3,40}

st2={1,2,3,4,5}

print(st1.issubset(st2))


st1={1,2,3,40}
st2={1,2,3,4,5}

symmetric_difference=st1.symmetric_difference(st2)

print(symmetric_difference)




text="this is atext to remove duplicate words this text is simple"

words=text.split("")

print(set(words))

