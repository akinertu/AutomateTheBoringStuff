
tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose','wwasasddmnak', 'asd']]

def maxrows():
    row_num = 0
    for i in range (len(tableData)):
        row_num = max(len(tableData[i]), row_num)
    return row_num

a = maxrows()

def columnwidth(k):
    width = 0
    for i in range (len(tableData[k])):
        width = max(len(tableData[k][i]), width)
    return width

for i in range (maxrows()):
    for k in range (len(tableData)):
        try:
            print(tableData[k][i].rjust(columnwidth(k)+1), end='')
        except:
            print(' '.rjust(columnwidth(k)+1), end='')
    print('')
