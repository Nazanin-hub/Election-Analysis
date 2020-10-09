# Election-Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of vote cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the county with the largest turnout.
6. Calculate the total number of votes for each county.
7. Calculate the percentage of votes for each county.
8. Determine the winner of the election based on popular votes.

## Resources
- Data source: election_results.csv
- Software: Python 3.8.3, Visual Studio Code,1.38.1

## Election-Audit Results:

 - How many votes were cast in this congressional election?
 
     - There were "369,711" vote cast in this election.
 
 - Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
 
    - Jefferson had "10.5%" of the votes and "38,855" number of votes.
    - Denver had "82.8%" of the votes and "306,055" number of votes.
    - Arapahoe had "6.7%" of the votes and "24,801 number of votes.
    
- Which county had the largest number of votes?
 
    - Denver had the largest number of votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    - Charles Casper Stockham recieved "23.0%" of the vote and "85,213" number of votes.
    - Diana DeGette recieved "73.8%" of the vote and "272,892" number of votes.
    - Raymon Anthony Doane recieved "3.1%" of the vote and "11,606" number of votes.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
 
    - Diana DeGette, who recieved "73.8%" of the vote and "272,892" number of votes.
    
#### Sample of my coding result 

                County Votes:
                Jefferson: 10.5% (38,855)
                Denver: 82.8% (306,055)
                Arapahoe: 6.7% (24,801)
                -------------------------
                Largest county turnout: Denver
                -------------------------
                Charles Casper Stockham: 23.0%(85,213)
                Diana DeGette: 73.8%(272,892)
                Raymon Anthony Doane: 3.1%(11,606)
                -------------------------
                Winner: Diana DeGette
                Winning Vote Count: 272,892
                Winning Percentage: 73.8%
                -------------------------
    
## Election-Audit Summary:

- I have developed a very fast, totally accurate, high cost effective script to analyze election results called "Elecsys". "Elecsys" can be used to process any election results   only by providing a simple excel of the votes.  Thus "Elecsys" can replace all traditional voting techniques that take a long time to count votes and usally suffers high error   rates. "Elecsys" is capable of providing you with various statistics based on the dataset of votes. For instace, given a data excel file with just three columns: Ballot ID,     County and Candidate, "Elecsys" will provide you with the following statistics:

    - The total number of votes cast.
    - The voter turnout for each county.
    - The percentage of votes from each county out of the total count.
    - The total number of votes each candidate won.
    - The percentage of votes each candidate won.
    - The county with the highest turnout.
    - Determine the winner of the election based on popular votes.
       
 - Modification:
 
    - Considering all states to get election result for whole country.
    - Considering the age of voters.
    - considering the gender of voters.
   Forexample, if I want to consider all states, some codes should be added to the previous one as below:
   
          Create a county list and county votes dictionary.
          state_options =[]
          state_votes ={}
        
          Write a decision statement that checks that the
          state does not match any existing state in the state list.
        
          if state_name not in state_options:

            Add the existing state to the list of states.
            state_options.append(state_name)

            Begin tracking the state's vote count.

            state_votes[state_name] = 0
            
          Add a vote to that state's vote count.
          state_votes[state_name] += 1
        
          write a repetition statement to get the state from the state dictionary.
          for state_name in state_votes:
            Retrieve the county vote count.
            votes = state_votes[state_name]
            Calculate the percent of total votes for the state.
            vote_percentage = float(votes) / float(total_votes) * 100

          Print the state results to the terminal.
          state_results = (f"{state_name}: {vote_percentage:.1f}% ({votes:,})\n")
         
          print(state_results)
  


