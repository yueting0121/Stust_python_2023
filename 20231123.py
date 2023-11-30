class employee:
    #初始化
    def __init__(self,name,id,salary,departmant):
        self.name = name
        self.id = id
        self.salary = salary
        self.departmant = departmant

    #計算加班時速>50計算加班費用
    def calculate_salary (self,hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.salary / 50)
            return self.salary + overtime_amount
        else:
            return self.salary

    def assign_department(self,new_department):
        self.department = new_department  

    #打印詳細資料
    def print_details(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.departmant}")

employee1 = employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = employee("MARTIN", "E7900", 50000, "SALES")
employee4 = employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_details()
employee2.print_details()
employee3.print_details()
employee4.print_details()

employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")
employee2.calculate_salary(52)
employee3.calculate_salary(60)

print ("  ")
print("Updated Employee Details:")
employee1.print_details()
employee2.print_details()
employee3.print_details()
employee4.print_details()