#  Non-Static Variables /Instance Variables


# 1)  Variable those are declared with self are mon-static variables are instance-variables 
# 2) Non-Static variable could not be define within the constructor also
# 3) These variables could be access in same class by using self







#  ----------------------------------------------------------------
 

#  Take the id, name, and sallary of employ from user and show the details using class

class Employee:

    # 1) Initialize the instance variables with provided values
    def __init__(self, id, name, salary):
        self.id = id

        self.name = name

        self.salary = salary

    # 2) Method to display the employee details
    def display_details(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
    
    
#  ----------------------------------------------------------------

#  Create an instance of Employee class and call display_details method

emp = Employee(101, "John Doe", 50000)

emp.display_details()

#  ----------------------------------------------------------------
