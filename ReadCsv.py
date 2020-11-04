import csv

with open('input.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=' ')
    for row in readCSV:
         print(row[0],row[1],row[2],row[3])

