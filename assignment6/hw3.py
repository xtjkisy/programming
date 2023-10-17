try:
    fileName = input("Enter a file name: ")
    scores = []

    with open(fileName, "r") as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                spam_score = float(line.split(":")[1])
                scores.append(spam_score)

except FileNotFoundError:
    print("Sorry, this file does not exist.")
    exit()

if not scores:
    print("No emails found in file.")
    exit()

average_score = sum(scores) / len(scores)

print(f"Average spam confidence: {average_score}")
