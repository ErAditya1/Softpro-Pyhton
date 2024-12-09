
str1 = 'Softpro'
# s,  o  removed

str2 = str1[1:-1]

i=0
for st in str2:
    subString=""
    for sub in str2:
        i+=1
        if sub in subString:
            continue
        else: 
            subString += sub
        
        print(subString)

print(i)