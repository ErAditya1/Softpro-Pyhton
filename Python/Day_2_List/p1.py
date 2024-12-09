#  Write a Python program to create a list of five nubers by taking input from user. Now find the secind Largest and second smalest number in the list.

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.sort()

second_largest = numbers[-2]

second_smallest = numbers[1]

print(f"Second largest number: {second_largest}")

print(f"Second smallest number: {second_smallest}")