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
#Initialize variables
    total_months = 0
    total_pl = 0
    greatest_increase = 0 
    greatest_month = str()
    greatest_decrease = 0 
    decrease_month = str()
    previous_row = None
    average_change = 0
    total_change = 0
    
#Calculate number of months
    for row in csv_reader:
        total_months += 1
    
#Calculate total profit/losses
        total_pl = int(row[1]) + total_pl
#Calculate average change
        if previous_row != None:
            total_change += int(row[1]) - int(previous_row)

#Calculate greatest increase
            if int(row[1]) - int(previous_row) > greatest_increase:
                greatest_increase = int(row[1]) - int(previous_row) 
   #Calculate greatest decrease
            if int(row[1]) - int(previous_row) < greatest_decrease:
                greatest_decrease = int(row[1]) - int(previous_row) 
        previous_row = int(row[1])
    average_change = total_change / (total_months-1)
        
     
    

#Print the results!
    print("Financial Analysis")
    print("-------------------------")
    print(total_months)
    print(average_change)
    print(total_pl)
    print(greatest_increase)
    print(greatest_decrease)
    