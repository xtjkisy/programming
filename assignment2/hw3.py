seconds = int(input("Enter seconds: "))
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(str(seconds) + " seconds is " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds")