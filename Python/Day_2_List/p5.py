# Write a python to create a list of five strings by taking input from user. Now find and dispaly the longest string in the list

strings = []

longest_string = ""

for i in range(5):
    string = input(f"Enter Strings {i+1}: ")
    strings.append(string)

for string in strings:
    for i in strings:
        if len(i) > len(string):
            longest_string = i
print (longest_string)