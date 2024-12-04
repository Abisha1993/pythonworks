from  re import finditer
text="fatcatrunsveryfasttocatththerat"
matcher=finditer("at",text)
for obj in matcher:
    print(obj.start(),obj.group())
