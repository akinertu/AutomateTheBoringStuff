message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

def isphonenumber(number):
    if (len(number) == 12 and 
        number[3] == '-' and 
        number[7] == '-' and
        number[0:3].isdecimal() and
        number[4:7].isdecimal() and
        number[8:].isdecimal()):
        return True
    else:
        return False

for i in range (len(message)):
    number = message[i:i+12]
    if isphonenumber(number):
        print(number)
    else:
        continue