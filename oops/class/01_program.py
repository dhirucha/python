class Student:
    def __init__(self, name, rollno, percentage):
        self.name = name
        self.rollno = rollno
        self.percentage = percentage
        
    def study(self):
        print("I am "+ self.name +" studying")
        
    def play(self):
        print("pdh liya ab khelna hai")


s1 = Student("Dhiru", 43, 90)
s1.study()
s1.play()

print(s1.percentage)
        