def compute_pay(input_hours, input_rate):
    if input_hours > 40:
        regular_pay = 40 * input_rate
        overtime_hours = input_hours - 40
        overtime_pay = overtime_hours * input_rate * 1.5
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = input_hours * input_rate
    return total_pay
    
try:
    input_hours = int(input("Enter hours: "))
    input_rate = int(input("Enter rate: "))
    salary = compute_pay(input_hours, input_rate)
    print("Salary:",salary)
except:
    print("Error, please enter numeric input")
