#  Write a python progam to create a function random(). This function returns random numbers from  1-10


def random():
    import random
    for i in range(10):
    
        value = random.randint(1,100)
        
        print(value, end=' ')

# print(random())
random();