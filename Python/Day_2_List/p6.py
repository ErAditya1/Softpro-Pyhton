# write a python program to create a list of five numbers by taking input from user. Now create a new list containing only the prime numbers from the original list 

numbers = []

for i in range(2,10):
    numbers.append(i)
    # numbers.append(int(input(f"Enter Numbers in a list {i+1}:")))
print(numbers)

new_list = []


for num in numbers:
    checkIsEven=-1;
    if num == 0 or num == 1:
        new_list.append(num)
    else:
        for i in range(2, num):
            if (num % i) == 0:
                checkIsEven = 0
                break
    if checkIsEven!=0:
        new_list.append(num)   

print(new_list)

   

    