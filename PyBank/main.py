# Create a Python script for analyzing the financial records of your company. 
# Given financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset has two columns: `Date` and `Profit/Losses`. 

import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join( 'Resources', 'budget_data.csv')

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header
    next(csvreader)

    # Pass the raw text data as a list
    csvdata = list(csvreader)

    #sets for column a and column b
    months = [row[0] for row in csvdata]
    profitloss = [int(row[1]) for row in csvdata]
    
    num_months = len(months)
    net_profitloss = sum(profitloss)

    change_profitloss = [[profitloss[i] - profitloss[i-1], months[i]] for i in range(1,num_months)]

    avg_change = [profitloss[i] - profitloss[i-1] for i in (range(1,num_months))]

    # Print total months in dataset //  Net Profit&Losses  // Changes in Profit/Loss // Grt Inc // Grt Dec
    print(" ")
    print(f"Financial Analysis")
    print(f"-------------------------------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: ${net_profitloss}")
    print(f"Average Change: ${int(sum(avg_change)/(num_months -1)):,.2f}")
    print(f"Greatest Increase in Profits: {max(change_profitloss)}")
    print(f"Greatest Decrease in Profits: {min(change_profitloss)}")
    print(f"-------------------------------------------")
    print ()

    # * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    # # # Store the file path associated with the file (note the backslash may be OS specific)

with open("Analysis/PyBank_Analysis.txt", "w") as f:

    f.write(" \n")
    f.write("Financial Analysis\n")
    f.write("-------------------------------------------\n")
    f.write(f"Total Months: {num_months}\n")
    f.write(f"Total: ${net_profitloss}\n")
    f.write(f"Average Change: ${int(sum(avg_change)/(num_months -1)):,.2f}\n")
    f.write(f"Greatest Increase in Profits: {max(change_profitloss)}\n")
    f.write(f"Greatest Decrease in Profits: {min(change_profitloss)}\n")
    f.write(f"-------------------------------------------\n")
    f.write (" \n")

    f.close()