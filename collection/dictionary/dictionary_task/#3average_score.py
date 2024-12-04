#3 calculate average score

students={"vipin":41,"jack":62,"jebin":98}
total=0
for i in students:
    total +=students[i]
    average=total/len(students)
    print(average)
