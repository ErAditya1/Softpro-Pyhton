#  write a pyhton program to create a function calc(), write code to find summation, substraction, multiplication and devision and return result in form of list. 

calc_list = []
def calc(op1, op2):
    calc_list.append(op1 + op2)
    calc_list.append(op1 - op2)
    calc_list.append(op1 * op2)
    calc_list.append(op1 / op2)
    return calc_list

    

print(calc(10, 5)) 