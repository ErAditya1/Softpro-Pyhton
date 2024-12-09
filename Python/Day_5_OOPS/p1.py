
class Aditya:
    
    name1 = 'Shubham Verma'
    def __init__(self, name) :  # Constructore
        self.name1 = name  # Instance variable
        print(self.name1)

    def display(self, name2):
        print('Hello', Aditya.name1)
        print('Hello ', name2)







name = input('Enter Your Name:');
nameObject = Aditya(name)

nameObject.display(name)
print(nameObject.name1)

