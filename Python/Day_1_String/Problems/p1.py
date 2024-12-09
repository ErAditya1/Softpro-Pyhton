# 1)Write a  Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

sample_string = 'The lyrics is not that poor!' or 'Not all reviews of the movie were poor' or 'Not everyone who appears to be poor is actually struggling.'
new_string =''
indexnot = sample_string.find('not')
indexpoor = sample_string.find('poor')


if indexnot < indexpoor and indexnot != -1 and indexpoor != -1:
    
    new_string = sample_string[0:indexnot] + "good" + sample_string[indexpoor+4:]


    print(new_string)
else : 
    
    print(sample_string)