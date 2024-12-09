#  Write a python program to create a list of five numbers by taking input from user. Now remove duplicates from the list and display the unique element

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

newList = []

for i in numbers:
    if i in newList:
        continue
    else:
        # numbers.append(i)
        newList.append(i)
        continue
        


print (newList)