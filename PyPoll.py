#Dependencies
import pandas as pd
import os
import csv

# The data we need to retrieve.

#Assign a variable for the file to load and the path to the file
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")

#open the election results and read the file. 
with open(file_to_load) as election_data:
    print("File is open.")

    #To do: read and analyze election data
    file_reader = csv.reader(election_data)

    # Print headers
    headers = next(file_reader)
    print(headers)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

#Use open() function with "w" mode to write data to file
with open(file_to_save, "w") as txt_file:

    # write data to the open file
    txt_file.write("Counties in the Election\n------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")



# Close the file. 

election_data.close()

#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote.


