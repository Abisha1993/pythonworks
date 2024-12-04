class Manager(Person,Employee):
    department:str
    def __init__(self,age,name,eid,salary,department):
        Person.__init__(self,age,name)
        Employee.__init__(self,eid,salary)
        self.department=department
    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print(self.department)
Manager_instance=Manager(32,"hari","eid",54000,"hr")
manager_instance.display_manager_info()

        


