#  Write a python program to create a function named substr(), in substr() function 
# pass a string and sub string. if substring is presented inthe string then return true else return false

def substr(s, sub):
    res = s.find(sub)
    if res>=0:
        return True
    else:
        return False





string=""" Write a python program to create a function named substr(), in substr() function 
pass a string and sub string. if substring is presented inthe string then return true else return false"""
substring = "Write"

print(substr(string, substring))