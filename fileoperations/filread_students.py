f1=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\datasets\\all_students.txt")
f2=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\datasets\\failed_students.txt")
all_students_set=set()
failed_students_set=set
for line in f1:
    line=line.rstrip("\n")
    all_students_set.add(line)
for line in f2:
    line=line.rstrip("\n")
    failed_students=all_students_set.difference(failed_students_set)
    print(passed_students)
