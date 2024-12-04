from re import fullmatch,findall,finditer
f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\processing_json\\regularexpressinons\\urls.txt")
content=f.read()
pattern="https?://[\w\S./]+"
urls=findall(pattern,content)
for url in urls:
    print(url)