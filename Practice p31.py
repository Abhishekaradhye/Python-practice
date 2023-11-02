

class emp():
    def __init__(self,name, eid, add):
        self.eid = eid 
        self.name = name
        self.add = add
        
class freelance(emp):
    def __init__(self, name, eid, add, email):
        super().__init__(name, eid, add)
        self.email = email

emp_1 = freelance('Abhishek Aradhye',92,'Pimpri','aa@gmail')

print('Id is ',emp_1.eid)
print('The Name is:', emp_1.name)
print('The Address is:', emp_1.add)
print('The Emails is:', emp_1.email)