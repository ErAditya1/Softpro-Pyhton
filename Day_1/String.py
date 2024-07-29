str1 = "Aditya Kumar from Government Polytechnic Aadampur Tarabganj Gonda";

# print(str1[5])             
    # [start:stop]

start_char = str1[0:6]   # starting charecter in a string
# print(start_char)  
last_char = str1[-5:]  # last characters in string
# print(last_char)

# print(str1[2::2]); # print on gap of 1

# [start:stop+1:step]

rev_string = str1[-1::-1] # reverse string >>> print from end of string on one gap

# print(rev_string)

# traversing of a string

ln = len(str1)
# print(ln)
# for x in str1:

    # print(x, end=" ")


#  Upper string 

upper_str = str1.upper();

# print(upper_str)

# lower string

lower_str = str1.lower();

print(lower_str)

# replace function

replace_str = str1.replace('Aditya', 'Shubham');

# print("replaced string : ", replace_str)

# count function

count_str = str1.count('a');

# print(count_str)

# split function

split_str = str1.split(" ");

print(split_str)
# print(type(split_str))
# print(len(split_str))

# join function 

join_str =' '.join(str1);

# print(type(join_str))
# print(join_str)


