 # Write a  Python program to create a person class. Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.
from datetime import date
class person():
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country 
        self.dob = dob
    def find_age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age 
    

VK = person("Virat Kohli", "India", date(1988,11,8))
NM = person("Narendra Modi", "India", date(1950, 9, 17))
CH = person("Chris Hemsworth", "Australia", date(1983, 8, 11))
AN = person("Anonymous Guy", "Future", date(2026,4,20))

print("Name : ", VK.name)
print("Country : ",VK.country)
print("Date of Birth : ", VK.dob)
print("Age : ", VK.find_age(),'\n')

print("Name : ", NM.name)
print("Country : ",NM.country)
print("Date of Birth : ", NM.dob)
print("Age : ", NM.find_age(),'\n')

print("Name : ", CH.name)
print("Country : ",CH.country)
print("Date of Birth : ", CH.dob)
print("Age : ", CH.find_age(),'\n')

print("Name : ", AN.name)
print("Country : ",AN.country)
print("Date of Birth : ", AN.dob)
print("Age : ", AN.find_age(),'\n')
        
