# Help a small, rural town modernize its vote counting process.
# Poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset has three columns: `Voter ID`, `County`, and `Candidate`. 

import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('Resources', 'election_data.csv')

with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header
    next(csvreader)

    # Pass the raw text data as a list
    csvdata = list(csvreader)

    #sets for voter column and candidate column
    voter_id = [row[0] for row in csvdata]
    candidates = [row[2] for row in csvdata]
    
    num_votes = len(voter_id)

    set_candidates = set(candidates)
    vot_book = { x : 0 for x in set_candidates}
    vot_percent = { x : 0 for x in set_candidates}
    for candidate in candidates :
        vot_book[candidate] = vot_book[candidate] + 1
        vot_percent[candidate] = round(((vot_book[candidate] / num_votes) * 100),2)
    
    win_candidate = None
    winner_votes = 0
    # (key,vale)
    for [candidate ,votes] in vot_book.items():
        if votes > winner_votes:
            win_candidate = candidate
            winner_votes = votes

    #Print List of Candidates // Percent of Votes // Total Votes // Winner
    print()
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {num_votes}")
    print("-------------------------")

    for key, value in vot_percent.items():
        print(f"{key}: {value}% {vot_book[key]}")

    print("-------------------------")
    print(f"Winner: {win_candidate}")
    print()
    
# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

   #Candidate
    #   -total votes:
    # a = {
    #     "Candidate":{"vots":0 ,"county" : ""},
    # "Candidate2":3  
    # }

    #list_candidates = ["name", "count"]