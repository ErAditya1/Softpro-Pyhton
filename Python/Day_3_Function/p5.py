#Write a python program to create a function named rev(), in rev() function pass a string and this function return reverse string.

str1 = "Hello World"

def rev(str):
    return str[-1::-1];

print(rev(str1))
