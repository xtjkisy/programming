while True:
    input_string = input("Please enter a string: ")

    if input_string.lower() == 'done':
        print("Bye!")
        break

    special_chars = ',.:!?'  
    for char in special_chars:
        input_string = input_string.replace(char, '')

    input_string = input_string.upper()

    print(input_string)
