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

    #change_profitloss = [[months[i], profitloss[i] - profitloss[i-1]] for i in range(1,num_months)]
    change_profitloss = [[profitloss[i] - profitloss[i-1], months[i]] for i in range(1,num_months)]
    #print(change_profitloss)

    # Grabs specific column from said list
    # max_ = max(change_profitloss, key=lambda col: col[1])
    # print(max_)

    # Removes brackets from list of lists, by creating a new list
    # test = 0
    # for i in range(len(change_profitloss)):
    #     change_profitloss[i][0]
    #     test += int(change_profitloss[i][0])
    # print(test)

    avg_change = [profitloss[i] - profitloss[i-1] for i in range(1,num_months)]
    # flat_list = []
    # for sublist in change_profitloss:
    #     for item in sublist:
    #         flat_list.append(item)
    # print(flat_list)
    # sum_test = [int(row[1]) for row in flat_list]

    
    #   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

    # Print total months in dataset //  Net Profit&Losses  // Changes in Profit/Loss
    # Grt Inc // Grt Dec
    print(" ")
    print(f"Financial Analysis")
    print(f"-------------------------------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: ${net_profitloss}")
    print(f"Average Change: ${int(sum(avg_change)/num_months)}")
    print(f"Greatest Increase in Profits: {max(change_profitloss)}")
    print(f"Greatest Decrease in Profits: {min(change_profitloss)}")
    print(f"-------------------------------------------")
    print ()

    #   ```text
    #   Financial Analysis
    #   ----------------------------
    #   Total Months: 86
    #   Total: $38382578
    #   Average  Change: $-2315.12
    #   Greatest Increase in Profits: Feb-2012 ($1926159)
    #   Greatest Decrease in Profits: Sep-2013 ($-2196167)
    #   ```

    # * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    # # # Store the file path associated with the file (note the backslash may be OS specific)
    # file = '../Resources/input.txt'

    # # Open the file in "read" mode ('r') and store the contents in the variable "text"
    # with open(file, 'r') as text:

    #     # This stores a reference to a file stream
    #     print(text)

    #     # Store all of the text inside a variable called "lines"
    #     lines = text.read()

    #     # Print the contents of the text file
    #     print(lines)
    # # 
    # # -----------------------------------------------