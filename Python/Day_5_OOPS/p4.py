# Static Variables/ Class variables

# 1) Static Variables are those variables that are defined in the class outside of the method
# 2) Static Variables are comman for all methods
# 3) Staic Variables of class could be accessed within the class and outside of the class

class Student:

    
    
    def set_studentsData(self, name, rollnumber):
        
        self.name = name
        self.rollnumber = rollnumber
        print(name)

    def set_studentsData(self, name):
        self.name = name
        print(name)


    def display_students(self):
        print("Roll Number of student", self.rollnumber)
        print("Name", self.name)


# Creating object of class Student


student = Student()
student.set_studentsData('Aditya' )

# student.display_students()


