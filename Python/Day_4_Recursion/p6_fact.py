#  write a python program to find the factorial of given number using 'Recursive'

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

fact = int(input("Enter a number: "))
print(factorial(fact))
'''
   5! = 5 * 4 * 3 * 2 * 1 = 120
   
n=1   1            =1
n=2   2*fact(1)    =2
n=3   3*fact(2)    =6
n=4   4*fact(3)    =24
n=5   5*fact(4)    =120

'''

