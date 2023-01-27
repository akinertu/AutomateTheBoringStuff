import pyinputplus as pyip


response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?')
while True:
    response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?')
    if response == 'no':
        break
print('Thank you. Have a nice day.')
