class Calculator:
     def __init__(self, n):
          self.n = n
          
     def square(self):
         print(f"The square:{self.n*self.n}")
     
     def cube(self):
         print(f"The cube:{self.n*self.n*self.n}")
     
     def squareroot(self):
         print(f"The squareroot:{self.n**1/2}")
     
     @staticmethod
     def hello():
         print("hello there")    


a = Calculator(4)        
a.square()
a.cube()
a.squareroot()
a.hello()