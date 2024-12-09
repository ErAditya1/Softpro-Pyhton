# 4)Write a Python program to remove characters that have odd index values in a given string.

sample_string = 'Hello Aditya Kumar'
newString=''
for i in range(len(sample_string)):
    if i % 2 == 0:
        newString += sample_string[i] 
# print (newString)

# or

newString = sample_string[0::2]

print(newString)