import csv

with open('input.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=" ")

    for row in readCSV:
        if(str(row).index(',')>0):
            print(str(row).index(','))
