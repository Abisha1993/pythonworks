f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\datasets\\fruits.txt","r")

fruit=[]

for line in f:
    fruit.append(line.rstrip("\n"))

print(fruit)

