count = 0
total = 0

while True:
    try:
        user_input = input("Enter a number: ")
        
        if user_input.lower() == "done":
            break
        
        number = float(user_input)
        total += number
        count += 1
    
    except:
        print("Invalid input. Enter a number.")
    

if count > 0:
    average = total / count
    print("Sum of input numbers:", total)
    print("Number of inputs:", count)
    print("Average of input numbers:",average)


https://nsmart.wsu.ac.kr/courses/31210
