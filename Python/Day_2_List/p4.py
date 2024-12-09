# write a python program to create a list of five numbers by takung input fro, user. now rotate list to the left by a given number of position.

numbers = []

for i in range(5):
    numbers.append(int(input(f"Enter number {i+1}: ")))
rotations = int(input("Enter number of rotations: "))

rotated_numbers = numbers[rotations:] + numbers[:rotations]

print("Rotated list:", rotated_numbers)