employee={"employeeid":1000,"name":"vipin","department":"hr","age":32,"salary":25000}

print(employee.get("department"))

#pop(key) remove

employee.pop("salary")

print(employee)


#return all keys

for k in employee.keys():

    print(k)


#fetch all values

for v in employee.values():
    print(v)


#fetch key and values
for k,v in employee.items():
    print(k,v)

