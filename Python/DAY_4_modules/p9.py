# write a pyhton program to create a module named temp conve. In temconv module create two function ctof() and ftoc(). ctof() function converts temperature from centigrade to forenheit and ftoc converts temperature from forenheit to celsius. Now import tempconve module and test ctof() and ftoc functions.

from tempconv import ctof,ftoc

print("Select Options:")

print("1. Convert Celsius to Fahrenheit")

print("2. Convert Fahrenheit to Celsius")

choice = input("Enter your choice (1/2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    temp = ctof(celsius)
    print(f"{celsius}°C is equal to {temp}°F")

elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temp = ftoc(fahrenheit)
    print(f"{fahrenheit}°F is equal to {temp}°C")