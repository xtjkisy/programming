def chop(myList):
  myList.remove(myList[0])
  myList.pop()
  return None

def middle(myList):
  newList = myList[1:-1]
  return newList

myList = [1, 2, 3, 4]
print("my list before call chop function =>", myList)
chop(myList)
print("my list after call chop function =>", myList)

myList = [1, 2, 3, 4]
print("my list before call middle function =>", myList)
middle(myList)
print("my list after call middle function =>", myList)

result = middle(myList)
print("new list after call middle function =>", result)


#-------------------------------------------------------------------------------------

with open("romeo.txt", "r") as fhand:
    myList = []
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in myList:
                myList.append(word)

    myList.sort()
    print(myList)

#-------------------------------------------------------------------------------------

with open("mbox.txt", "r") as fhand:
    total = 0
    for lines in fhand:
        if lines.startswith("From:"):
            lines = lines.replace("From:", "")
            print(lines.rstrip())
            total += 1
    print("Total %d lines were printed" %total)

#--------------------------------------------------------------------------------------


myList = []
while True:
    try:
        integer_input = input("Please enter an integer: ")
        if integer_input == "done":
            print("---------- Bye !! --------------")
            break
        else:
            integer_input = int(integer_input)
            myList.append(integer_input)
            sum = 0
            count = 0
            for integer_input in myList:
                sum += integer_input
                count += 1
                
            average = sum / count
            print(myList,", average = ", average)
    except ValueError:
        print("Please, enter numeric input")
