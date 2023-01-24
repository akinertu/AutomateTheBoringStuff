months = ({'01': '31','02': '28','03': '31','04': '30',
           '05': '31','06': '30','07': '31','08': '31','09': '30',
           '10': '31','11': '30','12': '31'})


# TODO detect dates in the DD/MM/YYYY
import re
text = r'Perşembe günü 26\01\2023 ofiste toplantı yapacığız. Sonra 30\02\2023 te tekrar toplanacağız.'
dateRegex = re.compile(r'(\d\d)\\(\d\d)\\(\d\d\d\d)')
dates = dateRegex.findall(text)
print(dates)

def validdate(date):
    if (int(date[2]) in range(2000,3000) and
        date[1] in months.keys() and
        int(date[0]) <= int(months[date[1]])):
        print('Valid date')
        return True        
    else:
        return False        

print(validdate(dates[0]))
        

# TODO detect if it is a valid date

def validdate(date):
    if (int(date[2]) in range(2000,3000) and
        date[1] in months.keys() and
        int(date[0]) <= int(months[date[1]])):
        print('Valid date')
        return True        
    else:
        return False  

for i in range (len(dates)):
    if validdate(dates[i]):
        continue
    else:
        dates.remove(dates[i])
print(dates)
        
        


# TODO store these strings into variables named month, day, and year


