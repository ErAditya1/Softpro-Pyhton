# write a python program to create a function search(),
#  in searsh function two parameters first, a list of ten numbers and second, a number to search.
#  if number is persent in the list return index of list otherwise return false,=.

def search(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 8

result = search(numbers, target)

if result is False:
    print(f"{target} not found in the list.")

else: 
    print(f"{target} found at index {result}.")
