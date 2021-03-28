# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has requested an election audit of a recent local congressional election. The audit is focused on determining the winning candidate, number of votes each candidate received, and determining voter turnout in each county in the preceinct.

#### Tasks
1. Calculate the total number of votes cast.
2. Get complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources Used
- Data Source: election_results.csv
- Software: Python 3.7.3, Visual Studio Code, 1.54.3

## Summary
The analysis of the election show that:
- There were 369,711 votes cast.
- Votes were concentrated in Denver county which comprised more than 82% of total votes (306,055).
- County Votes:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- Candidates receiving votes were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The Candidate results were:
  - Charles Casper Stockham received 23% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.

The winner of the election was Diana DeGette with 73.8% of the vote (272,892 votes).
- Winner: Diana DeGette
- Winning Vote Count: 272,892
- Winning Percentage: 73.8%

## Election Audit Summary
### 📊  Applying Script to Future Elections  :bar_chart:
As long as a few basic requirements are me, the Election Analysis script can be saved and modified to apply to future elections. 
Meeting the following requirements will improve script functionality:
- Election data must be stored in a .csv file. The script uses a Ptyhon module (csv) to read analyze data.
- Data should be stored vertically with each row representing a collection of associated data and each column representing a datapoint. 
  - Typically, the first column is used as an identifier, such as voter id, with columns to the right representing information associated with the identifier

Depending on the data available, future modifications could be applied to add additional summaries for more granular data. 
Fors example, the following portions of the script create variables to tabulate and store candidates, counties, and votes for each candidate and from each county.

#### Candidate Options and candidate votes
candidate_options = [] 

candidate_votes = {}
#### Counties and county votes
counties = []

county_votes = {}

If additional data is added to the election csv file the same variable layout could be used to find votes per city, per polling station, etc. by duplicating the variable layout above and adding a conditional block to the iterator which adds information to the new variables. Changing the reference in the code below to City, etc. would create a new collection of information that could be included in the analysis output. 

code()

        if county not in counties:
            # Add the existing county to the list of counties.
            counties.append(county)
            # Begin tracking the county's vote count.
            county_votes[county] = 0
         # Add a vote to that county's vote count.
         county_votes[county] += 1
```python
```

Additionally, the script could be modified to easily count the total number and unique number of items in each category. (i.e. candidate, county, city, etc.)

By changing the absolute index reference, an example of which can be found in line 49 of the script candidate_name = row[2], to a variable reference where the category index is referenced would increase the flexibility of the code. 

To apply this strategy the code would need to reference the csv headers which could then be used as an index. For example, if there were 6 categories the code could be re-written to ask a user what data they wanted to see, the user could type in "city" with city then being used as the index reference in the repetition (for loop), conditional (if statement), and logical statements (>,<,=) later in the script. 
