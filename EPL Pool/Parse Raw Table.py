import csv

def changeName(name):
    '''Change long names to shorter three letter names'''
    shortNames = ['Liverpool', 'LIV', 'Leicester City', 'LEI', 'Chelsea', 'CHE', 'Manchester City', 'MCI',
                  'Sheffield United', 'SHU', 'Arsenal', 'ARS', 'Bournemouth', 'BOU', 'Brighton and Hove Albion',
                  'BRI', 'Burnley', 'BUR', 'Crystal Palace', 'CRY', 'Newcastle United', 'NEW','Wolverhampton Wanderers',
                  'WOL', 'Tottenham Hotspur', 'TOT', 'Everton', 'EVE', 'Manchester United', 'MUN', 'West Ham United',
                  'WHU', 'Aston Villa', 'AVL', 'Watford', 'WAT', 'Southampton', 'SOU', 'Norwich City', 'NOR']
    for j in range(0, 40, 2):
        if name == shortNames[j]:
            return shortNames[j + 1]

def difference(top, bot):
    '''Calculate the difference between top and bottom pick teams'''
    for j in range(10, 210, 10):
        if top == newTables[j + 1]:
            topPts = int(newTables[j + 9])
        if bot == newTables[j + 1]:
            botPts = int(newTables[j + 9])
    return topPts - botPts


tables = newTables = []
with open('Raw table.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for line in readCSV:
        if line != '':
            tables.extend(line)

tables.pop()     #remove the last value in list which is ''

for j in range(10, 210, 10):
    newName = changeName(newTables[j + 1])
    newTables[j + 1] = newName


with open('Table data.csv', 'w') as csvWrite:
    for j in range(0, 210, 10):
        row10 = newTables[j: j + 10]
        data = ''
        for k in range(10):
            data += str(row10[k])
            if k < 9:
                data += ','
        csvWrite.write(data)
        csvWrite.write('\n')
