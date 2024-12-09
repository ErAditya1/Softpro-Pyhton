# WAPP to create a list of five numbers by taking input by users. Now create two seprate lists, one containing the numbers at even indices and the other containing the numbers

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_index = []
odd_index = []

for i in range(len(numbers)):
    if i % 2 == 0:
        even_index.append(numbers[i])
    else:
        odd_index.append(numbers[i])

print(f"Even indexed numbers: {even_index}")

print(f"Odd indexed numbers: {odd_index}")