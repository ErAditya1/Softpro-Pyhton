# 6)Write a program in python to take a sentence as input. Now count occurrence of ‘The’ word in given sentence

sentence = " Vedantu brings forth some of the most amazing kids' stories with colourful illustrations to make the most of the leisure reading of kids. "
sentence = input('Enter a string :>')
# count = sentence.count("The")
# count2 = sentence.count("the")

count = 0;

b = sentence.split();

for word in b:
    if word == 'The' or word == 'the':
        count += 1
print(count)      
