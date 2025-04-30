# str = input("Enter a string: ")

# rev = ""
# for strs in str:
#     rev = strs + rev

# print(rev)

num = 1234
reversed_num = 0

while num > 0:
    digit = num % 10 
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print(reversed_num)
    
    
    
        
# built in function
# text = "hello"

# rev_text = text[::-1]

# print(rev_text)