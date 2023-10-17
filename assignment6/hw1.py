try:
    input_fileName = input("Enter a file name: ")
    with open(input_fileName, 'r') as file:
        number = 1
        for line in file:
            print(f"LINE NUMBER : {number}")
            number += 1
except FileNotFoundError:
    print("Error: The specified file does not exist.")
