from re import findall
f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\processing_json\\regularexpressinons\\data.txt")
content=f.read()
pattern="[0-9]{2}/[0-9]{2}/[0-9]{2}"
all_dates=findall(pattern,content)
for date in all_dates:
    print(date)