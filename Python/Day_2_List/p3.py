# write a python program to create two lists of five numbers each by taking input by user. Now merge these two lists into a single list and short the merged list.

list1 = []
list2 = []

for i in range(5):
    num1 = int(input(f"Enter number {i+1} for list1: "))
    list1.append(num1)

for i in range(5):
    num2 = int(input(f"Enter number {i+1} for list2: "))
    list2.append(num2)

merged_list = list1 + list2

merged_list.sort(reverse=True)

print("Merged list:", merged_list)

