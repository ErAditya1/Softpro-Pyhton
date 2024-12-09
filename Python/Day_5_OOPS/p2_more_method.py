#  HOw to create more than one method inside a class
# how to create more than one object of the class

class hello:
    def method1(self, name1):
        print("Hello", name1)

    def method2(self):
        print("Hello, this is a static method")

obj1 = hello();
obj2 = hello();
obj3 = hello()
obj1.method1("Aditya")

obj2.method1("Shubham")

obj3.method2()
