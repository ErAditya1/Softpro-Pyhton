# Write a python program to generate a fibonacci series up to n numbers using recursion 

n = int(input("Enter number of terms for series:"))

'''

0, 1, 1, 2, 3, 5, 8, 13

a, b = 0, 1


a+b=a
0+1=1
  b+a=b
  1+1=2
    a+b=a
    1+2=3
      b+a=b
      2+3=5
        3+5=8
          5+8=13
                ...
  


'''

a=0
b=1 


def generateFibonacci(a,b,n):
    if n<=0:
        return;
    else:
        print(a,end=" ")
        generateFibonacci(b,a+b,n-1)

def fibonacciLoop(n):
    a=0
    b=1 
    
    for i in range(n):
        c=0
        c=a+b
        print(c,end=" ")
        
        a=b;
        b=c;
        
print("Through Recursion")
generateFibonacci(a,b,n)

print("\nThrough Loop")

fibonacciLoop(n)

