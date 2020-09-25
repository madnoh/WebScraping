import csv

picks = []
with open('Punters.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for line in readCSV:
        picks.extend(line)


for j in range (0, 51, 3):
    print(picks[j:j+3])


# with open('Punters.csv', 'r') as readFile:
#     for line in readFile:
#         print(line, end='')