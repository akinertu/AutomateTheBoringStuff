#DEFINITIONS
    keywords #such as names classNum
    identifiers #such as if, for, while
    statements # such as pi = 3.14

#GENERAL
    'Alice' + 'Bob' #String Concatenation
    'Alice' * 5 #String Replication
    print('Hello, world!') #print('Hello', end='') print('cats', 'dogs', 'mice', sep=',')
    myName = input() #input() function always returns a string
    print('It is good to meet you, ' + myName)
    len('hello')
    str(29)
    int('42') #round a floating-point number down.
    float(10)
    spam += 1 #spam = spam + 1

#FLOW STATEMENTS
    if name == 'Alice':
        else:
        elif age < 12:
    while spam < 5:
        break
        continue
    for i in range(5): #for i in range(0, 10, 2)
    import random #import random, sys, os, math
    random.randint(1, 10)
    #FUNCTIONS
    def hello(name):
        return 'It is certain'
        global eggs
        try:
        except ZeroDivisionError:

#LISTS, STRING(IMMUTABLE), TUPLE
    spam = ['cat', 'bat', 'rat', 'elephant'] #list  
    spam[2] #  is a list with an index
    spam[1:4] # is a list with a slice
    len(spam)
    spam[1] = 'aardvark' #Changing Values in a List with Indexes
    spam = spam + ['A', 'B', 'C'] #List Concatenation
    spam = ['X', 'Y', 'Z'] * 3 #List Replication
    del spam[2] #Removing Values from Lists
    'howdy' in ['hello', 'hi', 'howdy', 'heyas'] #The in and not in Operators
    for index, item in enumerate(supplies) #Instead of using the range(len(someList))
    random.choice(spam) #randomly selected item from the list.
    random.shuffle(spam) #reorder the items in a list
    spam.index('hello') # the index of the value is returned
    spam.append('moose') #adds the argument to the end of the list.
    spam.insert(1, 'chicken') #insert a value at any index in the list. 
    spam.remove('bat') #value to be removed from the list
    spam.sort() #number values or lists of strings can be sorted
    spam.sort(reverse=True) #sort the values in reverse order
    spam.sort(key=str.lower)
    spam.reverse() #Reversing the Values in a List 
        
    spam = ('hello', 42, 0.5) #tuple
    cheese = spam # The reference is being copied, not the list.
    list(('cat', 'dog', 5)) #tuple to list
    list('hello') #string to list
    cheese = copy.copy(spam) #duplicate copy of a mutable value like a list, import copy
    deepcopy() #list
#DICTIONARY
    spam = {'name': 'Zophie', 'age': 7}
    spam.keys()
    spam.values()
    spam.items()
    list(spam.keys()) #value returned from keys() and passes it to list()
    spam.get()
    spam.setdefault()

#MANIPULATING STRINGS
    spam = "That is Alice's cat." #Strings can begin and end with double quotes
    \' #Single quote
    \" #Double quote
    \t #Tab
    \n #Newline (line break)
    \\ #Backslash
    r'C:\Users\Al\Desktop '#raw string
    ''' '''#Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string.
    """ """ #Multiline Comments
    'Hello' in 'Hello, World' #
    'My name is %s. I am %s years old.' #string interpolation
    f'My name is {name}. Next year I will be {age + 1}.'
    upper(), lower(), isupper(), islower() # uppercase, lowercase, Boolean
    
    isalpha() #letters and isn’t blank?
    isalnum() #letters and numbers and is not blank?
    isdecimal() #only of numeric characters and is not blank?
    isspace() #spaces, tabs, and newlines and is not blank?
    istitle() #words that begin with an uppercase letter followed by only lowercase letters?
    ', '.join(['cats', 'rats', 'bats']) #join list of strings together into a single string value 
    'My name is Simon'.split('m') #returns a list of strings
    'Hello, world!'.partition('w') #returns a tuple of three substrings for the “before,” “separator,” and “after” substrings.
    before, sep, after = 'Hello, world!'.partition(' ') #creates tuple
    rjust(), ljust(), center() #justify 'Hello' in a string of total length 10
    strip(), rstrip(), lstrip() #strip off whitespace characters (space, tab, and newline
    ord('A') #Unicode code point. 
    chr(65) # https://youtu.be/sgHbC6udIqc
    import pyperclip
    pyperclip.copy('Hello, world!') #copy to clipboard
    pyperclip.paste() #paste clipboard

# REGULAR EXPRESSIONS https://pythex.org/
    import re
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #\d digit, r' raw string
    re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #\( escape chracter, r'^\d+$' all number
    phoneNumRegex.search('My number is 415-555-4242.')
    mo.groups() #retrieve all the groups at once (tuple)
    re.compile (r'Batman|Tina Fey') #Matching Multiple Groups with the Pipe
    re.compile(r'Bat(man|mobile|copter|bat)') #strings start with Bat:
    re.compile(r'Bat(wo)?man') #optional part
    re.compile(r'Bat(wo)*man') #Batwowowowoman
    re.compile(r'Bat(wo)+man') #at least one wo is required
    re.compile(r'(Ha){3,5}') #greedy: gives longest string
    re.compile(r'(Ha){3,5}?') #nongreedy
    .findall('Cell: 415-555-9999 Work: 212-555-0000') #matched objects in list of strings
    re.compile(r'.at')
    namesRegex.sub('CENSORED', 'Agent Alice') #replace any matches

    # Character Classes
    \d  #Any numeric digit from 0 to 9.
    \D  #Any character that is not a numeric digit from 0 to 9.
    \w  #Any letter, numeric digit, or the underscore character.  (Think of this as matching “word” characters.)
    \W  #Any character that is not a letter, numeric digit, or the underscore character.
    \s  #Any space, tab, or newline character. (Think of this as matching “space” characters.)
    \S  #Any character that is not a space, tab, or newline.

#INPUT VALIDATION
    import pyinputplus
    response = pyip.inputNum('Enter num: ', min=4)
    response = pyip.inputNum(blank=True)
    response = pyip.inputNum(limit=2, default='N/A') #trail limit
    response = pyip.inputNum(timeout=10) #time limit
    response = pyip.inputNum(blockRegexes=[r'[02468]$']) #won’t accept even numbers
    response = pyip.inputCustom(addsUpToTen) #custom validitation func
    
#READING AND WRITING FILES
    #Directory
        from pathlib import Path
        Path('spam', 'bacon', 'eggs')
        Path.cwd() #current working directory as a string value
        Path.home()
        import os
        os.chdir('C:\\Windows\\System32') #change cwd
        os.makedirs('C:\\delicious\\walnut\\waffles') #create new folders
        Path(r'C:\Users\Al\spam').mkdir() #To make a directory from a Path object
        Path.cwd().is_absolute()
        Path.home() / Path('my/relative/path')
        os.path.abspath(path) #convert a relative path into an absolute
        os.path.relpath(path, start) #string of a relative path from the start path to path
        p = Path('C:/Users/Al/spam.txt')
        p.anchor #'C:\\'
        p.parent #
        p.name #'spam.txt'
        p.stem #'spam'
        p.suffix #'.txt'
        p.drive #'C:'
        p.exists() #returns True if the path exists
        p.is_file() #returns True if the path exists and is a file
        p.is_dir() #returns True if the path exists and is a directory,
        Path.cwd().parents[0]
        os.path.dirname(path)
        os.path.basename(path)
        os.path.split(calcFilePath) #dir name and base name together tuple
        calcFilePath.split(os.sep) #['C:', 'Windows', 'System32', 'calc.exe']
        os.path.getsize(path) #size in bytes of the file
        os.listdir(path) #list of filename strings for each file in the path 
        list(p.glob('*.txt') # Lists all text files.
        list(p.glob('project?.docx')
    #Read and write
        p = Path('spam.txt')
        p.write_text('Hello, world!') #create a spam.txt file with the content 'Hello, world!'. 
        p.read_text() #reads and returns the contents
        helloFile = open('C:\\Users\\your_home_folder\\hello.txt') #a File object
        helloContent = helloFile.read()    
        open('bacon.txt', 'a') #append mode
        open('bacon.txt', 'w') # write mode
        baconFile.close() #After reading or writing a file, call the close() method before opening the file again
    #Saving Variables
        import shelve
        shelfFile = shelve.open('mydata')
        cats = ['Zophie', 'Pooka', 'Simon']
        shelfFile['cats'] = cats
        shelfFile.close()
        shelfFile = shelve.open('mydata')
        type(shelfFile) 
        shelfFile['cats'] #list(shelfFile.values())
        shelfFile.close()
#ORGANIZING FILES ch10
    import shutil
    shutil.copy(source, destination) #copy single folder
    shutil.copytree(source, destination) #copy entire folder
    shutil.move(source, destination) #move the file or folder
    os.unlink(path) #delete the file
    os.rmdir(path) #delete the folder
    shutil.rmtree(path) #remove the folder and all files 
    import send2trash
    send2trash.send2trash('bacon.txt') #sending files to the recycle bin
    os.walk() #returns lists of strings for the subfolder and filename variables
    import zipfile
    exampleZip = zipfile.ZipFile(p / 'example.zip') #reading zip file
    exampleZip.extractall() #extracting zip file
    
#DEBUGGING ch11
    raise Exception('Symbol must be a single character string.') #will store a variable named err.
    import traceback
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    assert ages[0] <= ages[-1] #“failing fast” 
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s  -  %(message)s')
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug() #Used for small details.
    logging.info() #record information on general events
    logging.warning() #indicate a potential problem that doesn’t prevent the program
    logging.error() #an error that caused the program to fail
    logging.critical() # indicate a fatal error
    logging.disable(logging.CRITICAL) #hiding log messages.
    logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

#WEB SCRAPING ch12
    import webbrowser
        webbrowser.open('https://inventwithpython.com/')
    import requests
        requests.get('https://automatetheboringstuff.com/files/rj.txt') #download web page
        raise_for_status() #to ensure that a program halts if a bad download occurs
        open('RomeoAndJuliet.txt', 'wb') #you must open the file in write binary mode
    import bs4
        exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
        soup.select('div') #All elements named <div>
        soup.select('#author') #The element with an id attribute of author
        soup.select('.notice') #All elements that use a CSS class attribute named notice
        soup.select('div span') #All elements named <span> that are within an element named <div>
        soup.select('div > span') #All elements named <span> that are directly within an element named <div>, with no other element in between
        soup.select('input[name]') #All elements named <input> that have a name attribute with any value
        soup.select('input[type="button"]') #All elements named <input> that have an attribute named type with value button        
    from selenium import webdriver
        browser = webdriver.Chrome()
        browser.get('https://inventwithpython.com')
        browser..find_elements(By.CLASS_NAME, "tomatoes") #Elements that use the CSS class name
        browser.find_elements(By.CSS_SELECTOR, '[name="q"]') #Elements that match the CSS selector
        browser.find_elements(By.ID, "fruits") #Elements with a matching id attribute value
        find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement") # used to track (or) find DOM element which has the focus in the current browsing context.
        browser.find_elements(By.TAG_NAME, 'div') #Elements with a matching tag name 
        userElem.send_keys('your_real_username_here')
        https://www.selenium.dev/documentation/webdriver/elements/finders/
        #Attribute or method 
        tag_name # The tag name, such as 'a' for an <a> element
        get_attribute(name) # The value for the element’s name attribute
        text #The text within the element, such as 'hello' in <span>hello </span>
        clear() #For text field or text area elements, clears the text typed into it
        is_displayed() #Returns True if the element is visible; otherwise returns False
        is_enabled() #For input elements, returns True if the element is enabled; otherwise returns False
        is_selected() #For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
        location #A dictionary with keys 'x' and 'y' for the position of the element in the page
        
        
#UTILITIES
    help(pyip.inputChoice) #find out more about functions