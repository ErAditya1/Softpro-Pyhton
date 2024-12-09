# 2). Write a Python program to remove the nth index character from a nonempty string.

string = "Hello World"
index = int(input("Enter an index to remove character"))

if len(string)==0:
    print("Cannot remove character from an empty string")
    exit()
if index > len(string):
    print("Endex is not a valid index")
    exit()
else:
    string = string[:index] + string[index+1:]

    print(string)
    