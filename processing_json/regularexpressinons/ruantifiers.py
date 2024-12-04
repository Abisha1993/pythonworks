from re import finditer
text="abbbababbabaaaab"
pattern="a{2}"
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())