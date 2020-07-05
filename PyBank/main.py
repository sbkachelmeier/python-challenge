#Import files
import os
import csv
file = os.path.join("Resources", "budget_data.csv")

#Open the CSV file
file = 'Resources/budget_data.csv'
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#Read the header row
    csv_header = next(csv_reader)
#Calculate total number of months
    months = len(list(csv_reader))
    print(months)
    
#Calculate total profit/losses
    # total = 0
    # for row in csv.reader(file)):
    #     total = row[1] + total
        
        #print(total)
#Calculate greatest change
#Calculate greatest increase
    greatest_increase = max
#Calculate greatest decrease
    