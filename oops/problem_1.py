class Programmer:
    company = 'Microsoft'
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = Programmer("Dheeraj",120000,421102)
print(p.name,p.salary,p.pin, p.company)
r = Programmer("Rohan",110000,421102)
print(r.name,r.salary,r.pin, r.company)