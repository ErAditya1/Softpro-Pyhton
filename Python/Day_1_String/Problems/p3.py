# 3)Write a  Python program to change a given string to a newly string where the first and last chars have been exchanged.

String = 'Write a  Python program to change a given string to a newly string'
newString = "";

if len(String) <= 1:
    print("Can't exchange strings character")

else:
    newString = String[len(String)-1]+ String[1:-1] + String[0]

print(newString)