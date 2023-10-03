def calculate_grade(score):
    if score > 100 or score < 0:
        print("Error, please enter numeric input between 0 and 100")
    elif score >= 90:
        print("Grade is A")
    elif score >= 80:
        print("Grade is B")
    elif score >= 70:
        print("Grade is C")
    elif score >= 60:
        print("Grade is D")
    else:
        print("Grade is F")
try:
    score = int(input("Enter Score: "))
    grade = calculate_grade(score)
except:
    print("Error, please enter numeric input between 0 and 100")
