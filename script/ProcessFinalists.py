import csv
import re
import io
import collections

## A script to process the Reader feedback
## 0. Create key-value pair for each entry to track the score.
## 1. Tally up the score for each entry (first gets 5 points, second gets 4 points, etc)
## 2. Manually go through and add the FINALIST tag, and copy that entry's text into the new finalists file for the Judge

entryScores = {}

# Last minute contributions
number1 = "We Are Centaurs"
number2 = "Housecat-astrophy"
number3 = "Sustenance & Sustainability" 
number4 = "Parsley Sage"
number5 = "Beloved Leader"

if number1 in entryScores: 
    entryScores[number1] = entryScores[number1] + 5  
else: 
    entryScores[number1] = 5

if number2 in entryScores: 
    entryScores[number2] = entryScores[number2] + 4  
else: 
    entryScores[number2] = 4

if number3 in entryScores: 
    entryScores[number3] = entryScores[number3] + 3  
else: 
    entryScores[number3] = 3

if number4 in entryScores: 
    entryScores[number4] = entryScores[number4] + 2
else: 
    entryScores[number4] = 2

if number5 in entryScores: 
    entryScores[number5] = entryScores[number5] + 1  
else: 
    entryScores[number5] = 1


if number1 in entryScores: 
    entryScores[number1] = entryScores[number1] + 5  
else: 
    entryScores[number1] = 5

with open('top5.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:

        number1 = row[3]
        number2 = row[8]
        number3 = row[13]
        number4 = row[18]
        number5 = row[23]

        if number1 in entryScores: 
            entryScores[number1] = entryScores[number1] + 5  
        else: 
            entryScores[number1] = 5

        if number2 in entryScores: 
            entryScores[number2] = entryScores[number2] + 4  
        else: 
            entryScores[number2] = 4

        if number3 in entryScores: 
            entryScores[number3] = entryScores[number3] + 3  
        else: 
            entryScores[number3] = 3

        if number4 in entryScores: 
            entryScores[number4] = entryScores[number4] + 2
        else: 
            entryScores[number4] = 2

        if number5 in entryScores: 
            entryScores[number5] = entryScores[number5] + 1  
        else: 
            entryScores[number5] = 1

with open('finalistSCORES.csv', 'w') as f:
    f.write("%s,%s\n"%("Name","Score"))
    for key in entryScores.keys():
        f.write("%s,%s\n"%("\""+key+"\"",entryScores[key]))


