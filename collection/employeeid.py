employee={"id":1000,"name":"vipin","salary":20000,"department":"hr","experience":2}

print(employee["salary"])
      

# add contact as12365622

employee["contact"]=123456789

print(employee)


#if experiece > 5 salary 100000 else salary 50000

if employee["experience"]>5:

   employee["salary"]+=10000

else:
   employee["salary"]+=5000

   print(employee)
