'''Create an Employee class that: Stores name, ID, and salary. Automatically assigns unique IDs. Tracks how many employees are created.
Gives bonuses based on designation. Prevents invalid salary input. Supports search of employee by ID (via class method).'''

class Employee():
    __id_counter = 101
    _employees_list = []

    def __init__(self,name,salary, designation):
        if salary <= 0:
            raise Exception('Salary must be greater than 0')
        self.id = Employee.__id_counter
        self.name = name
        self.salary = salary
        self.designation = designation
        Employee.__id_counter += 1
        Employee._employees_list.append(self)

    def apply_bonus(self):
        bonus_map = {
            'Manager': 0.2,
            'Developer': 0.15,
            'Intern': 0.05,
            'Tester': 0.1,
            'Accountant': 0.15
        }

        bonus = bonus_map.get(self.designation, 0.1)
        self.salary += self.salary * bonus

        print(f"Bonus Updated ! New salary of {self.name} is Rs.{self.salary:.2f} ...")

    @classmethod
    def total_employees(cls):
        return len(cls._employees_list)
    
    @classmethod
    def find_by_id(cls,eid):
        for emp in cls._employees_list:
            if emp.id == eid:
                return emp
            
        return None

        
try:
    emp1 = Employee("Abhi", 50000, "Developer")
    emp2 = Employee("Ram", 60000, "Manager")
    emp3 = Employee("Hardik", 10000, "Intern") 
except Exception as e:
    print(e)

print(emp1.apply_bonus())
employ = Employee.find_by_id(emp2.id)
print(f"📊 Total Employees: {Employee.total_employees()}")
