#  HOw to create more than one method inside a class
class A:
    def addition(self, a,b):
    
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b


obje1 = A();

print(obje1.addition(5, 7));

print(obje1.subtraction(10, 3));

print(obje1.multiplication(4, 5));
        

