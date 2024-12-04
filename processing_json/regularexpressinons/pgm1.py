from re import finditer
text="I have 3cars,2 bike and 1 cycle"
pattern="\d"
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())
