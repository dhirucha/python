class Student:
    def __init__(self, name, rollno, percentage):
        self.name = name
        self.rollno = rollno
        self.__percentage = percentage
        
    def study(self):
        print("I am "+ self.name +" studying")
        
    def play(self):
        print("pdh liya ab khelna hai")
        
    def __str__(self):
        return print("Hi i am here")
    
    def __add__(arg1, arg2):
        resultReal = 0
        resultImg = 0
        
    def getMarks(self):
        return self.__percentage


s1 = Student("Dhiru", 43, 90)
s1.study()
s1.play()
s1.getMarks()

print(s1.percentage)
        