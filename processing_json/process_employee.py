from json import load
f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\datasets\\employeejson.txt")
data=load(f)
for emp in data:
    print(emp)