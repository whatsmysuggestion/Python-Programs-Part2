import csv

with open('input.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=" ")

    temp500=""
    temp500Count=0
    temp700=""

    for row in readCSV:
        if((row[3]=='500')):
            temp500=temp500+","+row[0]
            temp500Count =temp500Count+1

        elif((row[3]=='700')):
            temp700 = temp700 + "," + row[0]

print("500 Assigned to",temp500)
print("500 Connected to",temp500Count," number of ports")
print("700 Assigned to",temp700)