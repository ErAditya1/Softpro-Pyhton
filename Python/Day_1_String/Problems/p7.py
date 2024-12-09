# 7)Write a program in python to take full name as input. Now display short name of user.
# example

name = input("Enter your name:>")

listedName = name.split()
shortName =''

for i in range(len(listedName)):
    if(i== len(listedName)-1):

        shortName += listedName[i]
        continue;
    shortName += listedName[i][0].upper() + '.' ;

print(shortName)