import csv
import random

diction = {}

#parsing occupation rows
with open('occupations.csv', 'r') as csv_file:
    occupations = csv.reader(csv_file)
    #putting the rows into diction mapping job to percent value
    temp = 0
    for row in occupations:
        diction[row[0]] = row[1]
        if temp == 0:
            #remove first value in diction because we don't need it
            diction.pop("Job Class")
            temp += 1
    
print(diction)

#def choose_occupation(d):
    

