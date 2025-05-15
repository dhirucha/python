def palindrome(n):
     reverse = str(n)
     
     return reverse == reverse[::-1]
     
    
    

number = int(input("Enter a number:"))

if palindrome(number):
    print("Number is palindrome")
else:
    print("Not a palindrome")
     
     
        
