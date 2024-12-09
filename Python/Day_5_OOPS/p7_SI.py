# WAP to calculate the simple inttrest of any amount, take the required inputs from the user
# then create instance variables


class SimpleIntrest: 
    
    def set_instance(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_intrest(self):
        return (self.principal * self.rate * self.time) / 100

# Create an instance of the class and calculate the simple intrest

si = SimpleIntrest()
si.set_instance(1000, 5, 2)
intrest = si.calculate_intrest()
print(f"Simple Interest: {intrest}")