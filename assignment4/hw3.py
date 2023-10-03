def num_divide3(num):
    count = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1
    return count

while True:
    input_num = input("Enter a positive integer: ")

    if input_num.lower() == 'done':
        print("bye!!")
        break

    try:
        num = int(input_num)
        if num <= 0:
            print("please enter a positive number")
        else:
            result = num_divide3(num)
            print("numbers divisible by 3 among numbers from 1 to", num,":", result)
    except :
        print("please enter a positive number")
