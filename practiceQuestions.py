Practice questions

# ch.12
# 1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
    webbrowser.open() launches web browser,
    request downloads files and web pages,
    bs4 parses html
    selenium can launch and browse web pages
# 2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?
    requests.get() returns response object, it has text attribute
# 3. What requests method checks that the download worked?
    raise_for_status()
# 4. How can you get the HTTP status code of a requests response?
    status_code
# 5. How do you save a requests response to a file?
    saveFile = open('filename.html', 'wb')
    for chunk in res.iter_content(100000):
    saveFile.write(chunk)
# 6. What is the keyboard shortcut for opening a browser’s developer tools?
    F12
# 7. How can you view (in the developer tools) the HTML of a specific element on a web page?
    Inspect Element
# 8. What is the CSS selector string that would find the element with an id attribute of main?
    .select('#main')
# 9. What is the CSS selector string that would find the elements with a CSS class of highlight?
    .select('.highlight')
# 10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
    .select('div div')
# 11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
    .select('button[value="favorite"]')
# 12. Say you have a Beautiful Soup Tag object stored in the variable spam for 
    # the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?
    soup.getText()    
# 13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?
    linkElems.attribute
# 14. Running import selenium doesn’t work. How do you properly import the selenium module?
    from selenium import webdriver
# 15. What’s the difference between the find_element_* and find_elements_* methods?
    first matching element as a WebElement object
    list of all matching elements as WebElement objects.
# 16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?
    click() send_keys()
# 17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?
    submit() method on any element within a form submits the form
# 18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?
    forward(), back(), and refresh() WebDriver object

# ch.13
# 1. What does the openpyxl.load_workbook() function return?
    workbook object
# 2. What does the wb.sheetnames workbook attribute contain?
    worksheet object
# 3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?
    wb['Sheet1']
# 4. How would you retrieve the Worksheet object for the workbook’s active sheet?
    wb.active
# 5. How would you retrieve the value in the cell C5?
    sheet['C5'].value or sheet.cell(row=5, column=3).value
# 6. How would you set the value in the cell C5 to "Hello"?
    sheet['C5'] = 'Hello' 
# 7. How would you retrieve the cell’s row and column as integers?
    cell.row and cell.column
# 8. What do the sheet.max_column and sheet.max_row sheet attributes hold and what is the data type of these attributes?
    Returns maximum number of rows and columns as integers
# 9. If you needed to get the integer index for column 'M', what function would you need to call?
    openpyxl.cell.column_index_from_string('M')
# 10. If you needed to get the string name for column 14, what function would you need to call?
    openpyxl.cell.get_column_letter(14)
# 11. How can you retrieve a tuple of all the Cell objects from A1 to F1?
    sheet['A1':'F1']
# 12. How would you save the workbook to the filename example.xlsx?
    wb.save('example.xlsx')
# 13. How do you set a formula in a cell?
    wb.active['A1'] = '=B1-C1'
# 14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?
    When calling load_workbook(), pass True for the data_only keyword argument.
# 15. How would you set the height of row 5 to 100?
    sheet.row_dimensions[5].height = 100    
# 16. How would you hide column C?
    sheet.column_dimensions['C'].hidden = True
# 17. What is a freeze pane? 
    fixed row or column
# 18. What five functions and methods do you have to call to create a bar chart?
    openpyxl.chart.Reference(), openpyxl.chart.Series(), openpyxl.chart.BarChart(), 
    chartObj.append(seriesObj), and add_chart()