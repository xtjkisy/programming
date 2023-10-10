input_string = input("Please enter string: ")

uppercase = 0
lowercase = 0
number = 0
other = 0

for char in input_string:
    if char.isupper():
        uppercase += 1 
    elif char.islower(): 
        lowercase += 1
    elif char.isdigit(): 
        number += 1
    else:  
        other += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Numbers:", number)
print("Other characters:", other)
