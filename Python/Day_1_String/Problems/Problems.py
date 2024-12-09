
# Write a program in python to take a string as input  and convert it into Upper ,Lower and title format

# str1 = input("enter the data");

# upper_str = str1.upper(); 

# print("Upper Case : ", upper_str);

# lower_str = str1.lower();

# print("Lower Case : ", lower_str);

# title_str = str1.title();

# print("Title Case : ", title_str);

# Write a program in python to take a string as input  and check wheather a string is palindrom or not

# str2 = input("Enter the data");


# if str2 == str2[::-1]:

    # print("The string is a palindrome");
# else: 
    # print("The string is not a palindrome");



# Convert the string in title format by logic

# str3 = input("Enter A string for title format:>");
str3 = "Enter A string for title format"

words = str3.split()
title_str=""
# print(words)
for word in words:
    # print(word.capitalize(), end=' ')
    title_str+=" "+word.capitalize();
# print(title_str);

