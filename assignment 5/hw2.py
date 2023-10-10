input_words = input("Enter string: ")

print("Input string =", input_words)

length = len(input_words)
index = length - 1

while index >= 0:
    print(input_words[index])
    index -= 1
