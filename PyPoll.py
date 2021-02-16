# The data we need to retrieve
# 1. The total number of votes cast. 
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the lection based on popular vote 

# Add our dependencies
import os 
import csv 

# Assign a variable to load a file from a path .
file_to_load = 'Desktop/Analysis_Projects/election_analysis/Resources/election_results.csv'

# assign a variable to save the file to a path 
file_to_save = 'Desktop/Analysis_Projects/election_analysis/analysis/election_analysis.txt'

# Open the election results and read the file
with open(file_to_load) as election_data:
     
     # To do: read and analysis the data here
     csvreader = csv.reader(election_data, delimiter=',')
     
     csv_header = next(csvreader)
     print(f"CSV Header: {csv_header}")

     for row in csvreader:
      print(row)

# Using a with statement open the file s a text file. 
#with open(file_to_save, "w") as txt_file:  
   # Write three counties to the file. 
   #txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")




          