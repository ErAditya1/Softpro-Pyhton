def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a/b
    
def add_list(list):
    result = 0
    for num in list:
        result += num
    return result