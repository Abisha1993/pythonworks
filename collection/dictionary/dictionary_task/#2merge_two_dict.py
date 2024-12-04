#2  merge two dictionaries

a={"product":"apple","price":1200}
b={"quantity":"2kg","piece":30}

a.update(b)
print(a)
merged={**a,**b}
print(merged)

