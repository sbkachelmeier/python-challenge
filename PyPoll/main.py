#Import files
import os
import csv
file = os.path.join("Resources", "election_data.csv")

#Open the CSV file
file = 'Resources/election_data.csv'
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#Read the header row
    csv_header = next(csv_reader)
#Calculate total votes
    total_votes = 0
    candidates = {}
    for row in csv_reader:
        total_votes += 1
        
#Calculate votes per candidate 
        
        name = row[2]
        if name not in candidates:
           candidates[name] = 1
        else:
            candidates[name] = candidates[name] + 1
    for candidate in candidates:
        vote_count = candidates[candidate]
         
#Print the results!
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    winner_total = 0 
    winner_name = str()
    for candidate in candidates:
        vote_count = candidates[candidate]
        percentage = "{:.0%}".format(vote_count/total_votes)
        if winner_total < vote_count:
            winner_total = vote_count
            winner_name = candidate
        
        print(f"{candidate}: {vote_count} {percentage}")
    print("-------------------------")
    
    print("The winner is... ")
    print(winner_name)



    



