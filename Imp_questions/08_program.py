number = input("Enter a five digit number: ")


if len(number) != 5 or not number.isdigit():
    print("Invalid input! Please enter a five digit number.")
    
else:
    reversed_number = number[::-1]
    
    print("Reversed number: ", reversed_number)
    
    if number == reversed_number:
        print("The number is palindrome.")
    else:
        print("Not a palindrome.")