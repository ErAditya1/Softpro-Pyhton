# wap to calculate area and perimeter of a rectangle, take length and breadth of a reactangle from the user and ctreate the instance of varible,


class Claculate:
    def set_instance(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)
    

length = int(input("Enter the length of the rectangle: "))

breadth = int(input("Enter the breadth of the rectangle: "))

rectangle = Claculate()

rectangle.set_instance(length, breadth)

area = rectangle.calculate_area()

perimeter = rectangle.calculate_perimeter()

print(f"Area of the rectangle: {area}")

print(f"Perimeter of the rectangle: {perimeter}")
