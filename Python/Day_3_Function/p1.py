#  Write a python program to create two functions area() and peri() to find area and perimeter of rectangle

def peri(l,b):
    return (2*(l+b))
def area(l,b):
    return (l*b)



length = int(input("Enter the length:"))

breadth = int(input("Enter the breadth:"))

area = area(length, breadth);

peri = peri(length, breadth);

print(f"Area of rectangle: {area}")

print(f"Perimeter of rectangle: {peri}")