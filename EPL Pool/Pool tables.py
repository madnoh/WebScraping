import csv

def difference(top, bot):
    '''Calculate the difference between top and bottom pick teams'''
    for j in range(10, 210, 10):
        if top == newTables[j + 1]:
            topPts = int(newTables[j + 9])
        if bot == newTables[j + 1]:
            botPts = int(newTables[j + 9])
    return topPts - botPts

def importPunters():
    with open('Punters.csv' 'r') as p:
        readCSV = csv.reader(p, delimiter = ',')
        for line in readCSV:

tables = newTables = []
with open('Table data', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for line in readCSV:
        if line != '':
            tables.extend(line)

tables.pop()     #remove the last value in list which is ''

# with open('Table data.csv', 'w') as csvWrite:
#     for j in range(0, 210, 10):
#         row10 = newTables[j: j + 10]
#         data = ''
#         for k in range(10):
#             data += str(row10[k])
#             if k < 9:
#                 data += ','
#         csvWrite.write(data)
#         csvWrite.write('\n')
