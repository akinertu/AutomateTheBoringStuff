# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
text = 'My name is AL SWEIGART and I am 4,000 years old.'
vowels = ('a', 'e', 'i', 'o', 'u', 'y')


words = text.split(' ')

for i in range (len(words)):
    if words[i][0].isdecimal():
        continue
    elif words[i][-1].isalpha(): 
        if words[i][0].isdecimal():
            continue
        elif words[i][0].lower() in vowels:
            words[i] += 'yay'
        else:
            words[i] = words[i][1:] + words[i][0] + 'ay'
    else:
        if words[i][0].lower() in vowels:
            words[i] = words[i][:-1] + 'yay' + words[i][-1]
        else:
            words[i] = words[i][1:-1] + words[i][0] + 'ay' + words[i][-1]
        
       
sentence = ' '.join(words)
print(sentence)


