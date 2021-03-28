#Dependencies
import pandas as pd
import os
import csv

# The data we need to retrieve.

#Assign a variable for the file to load and the path to the file
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare candidates list
candidate_options = []
# Candidate votes
candidate_votes = {}

# declare variables for winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file. 
with open(file_to_load) as election_data:
    
    #To do: read and analyze election data
    file_reader = csv.reader(election_data)

    # Print headers
    headers = next(file_reader)

    # loop through rows in vote spreadsheet and count votes
    for row in file_reader:
        #2. Add total votes
        total_votes += 1

        # Get candidate name from each row (index row list)
        candidate_name = row[2]

        # check if candidate is in the option list already
        if candidate_name not in candidate_options:

            # append names to candidate option list
            candidate_options.append(candidate_name)

            # create key to track votes (applies value to key in candidate_votes dictionary)
            candidate_votes[candidate_name] = 0

        # add votes for candidates
        candidate_votes[candidate_name] += 1

# get candidate names from options list and tally votes
for candidate in candidate_options:
    # get votes for each candidate
    votes = candidate_votes[candidate]
    #calculate percentage of vote
    vote_percentage = (float(votes) / float(total_votes))
    
    # print the results of the election
    print(f"{candidate} received {vote_percentage:.1%} of the vote ({votes:,})\n")

    #Determine winning vote count and candidate
    # compare vote count / find winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

# print winning candidate summary
winning_candidate_summary = (
    f"--------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1%}\n"
    f"--------------------------------")
print(winning_candidate_summary)

# print(f"{winning_candidate} won the election with {winning_percentage:.1%} of the vote.")

# Close the file. 
election_data.close()