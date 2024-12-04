from re import finditer
text="abababbaab"
pattern="ab"
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())

    