# Election Analysis

## Project Overview 
By direction of The Colorado Board of Elections, we were to perform an audit of a recent local congressional district by completing the following tasks: 
1. The total number of votes cast 
2. Compile a complete list of candidates who received votes 
3. Calculate the percentage of votes each candidate won
4. Calculate the total number of votes each candidate received 
5. Determine the winner of the election based on the popular vote 

## Resources
- Data Source: [election_results.csv](Resources/election_results.csv) 
- Software: Python 3.7.6, Visual Studio Code 1.53.2

## Summary 
The analysis of the election shows that: 
- There were 369,711 total votes cast 
- The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
  - Diana DeGette received 73.8% of the votes and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes 
- The winner of the election was: 
  - Diana DeGette who received 73.8% of the votes and 272,892 votes
 
## Challenge Overview
The election commission requested additional data on the results of the counties in the election. They asked for the following data about the counties:
1. The voter turnout for each county
2. The percentage of votes from each county out of the total votes
3. The county with the largest turnout

### Election-Audit Results: 
-	There were 369,711 total votes cast 
-	County votes: 
    -	Jefferson: 10.5% (38,855 votes)
    -	Denver: 82.8% (306,055 votes)
    -	Arapahoe: 6.7% (24,801 votes)
-	The county with the largest number of votes was Denver
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
  - Diana DeGette received 73.8% of the votes and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes 
- The winner of the election was: 
  - Diana DeGette who received 73.8% of the votes and 272,892 votes

#### Complete election results can be found [here](analysis/election_results.txt). 

## Challenge Summary
### Election-Audit Summary: 
While this script was created for a specific audit for The Colorado Board of Elections, it can be modified to fit any election. For example, if the script was used to audit the results of the state’s gubernatorial election, we can modify the existing script to find the candidate’s and voter’s associated political party to see which party had the highest number of votes. Another example of how this script can be modified to fit any election would be to find the method each voter used to vote. Since there are multiple ways to vote (e.g., mail-in ballot, in-person, absentee, etc.), we can find out which method is used the most/least to make decisions on where to place resources to improve voter experience and engagement in future elections. 
