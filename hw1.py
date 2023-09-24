try:
    input_hours = int(input("Enter Hours: "))
    input_rate = int(input("Enter rate: "))
    # salary = (input_hours * input_rate)
except:
    print("Error,plese enter a numeric number")

else:
    if input_hours > 40:
        overtime_hours = input_hours - 40
        overtime_rate = input_rate * 1.5
        salary = (40 * input_rate) + (overtime_hours * overtime_rate)
        print(float(salary))
    else:
        salary = input_hours * input_rate
        print(salary)