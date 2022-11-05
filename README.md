# Election Analysis 

## Project Overview 
A Colorado Board of Elections employee has asked for me to perform the following functions in order to audit an election. 
  1. Calculate the total numberr of votes casts
  2. Print a complete list of candidates who received votes
  3. Calculate the total number of votes each candidate received 
  4. Calculate the percentage of votes each candidate won
  5. Determine the winner of the election based on the popular vote 
  
## Resources 
  * Data Source: election_results.csv
  * Software: Pyton 3.9.0, Visual Studio Code, 1.72
  
## Summary 
  * There were 369,711 votes cast in the election. 
  * The candidates were: 
    * Charles Casper Stockham
    * Diana DeGette 
    * Raymon Anthony Doane
  * The candidate results were:
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606) 
  * The winner of the elction was: 
    * Diana DeGette, who received 73.8% of the popular vote and 272,892 number of votes. 
    
 ## Challenge Overview 
 A Colorado Board of Elections employee has asked for me to perform the following functions in order to audit an election. After receiving the intitial data, the election commission requested a few more pieces of information. 
  1. Calculate the voter turnout for each county
  2. Calculate the percentage of votes deom each county out of the total vote count
  3. Determine the country with the highest turnout
  
  ## Challenge Results 
  <p align="center">
  <img width="400" height="600" src="https://github.com/jcarter211/election-analysis/blob/main/Supporting%20Materials/Election_Results.png">
</p>

 The results of the election are seen above. With our code, we easily identified that Denver had the largest county turnout and Diana DeGette won the elcetion, winning 73.8% of the votes. She had an overwhelming amount of the majority. 
 
 In order to add the county to our election audit, we needed to add code that supported the information about each county. To begin, we first had to identify a new list and dictionary: election_counties, county_votes. We then needed to add the counties to the election_counties list and add the updated list to the dictionary. Once the counties were added to the dictionary, we began to track and add votes to the county's vote count. 
 
 <p align="center">
  <img width="400" height="600" src="https://github.com/jcarter211/election-analysis/blob/main/Supporting%20Materials/Tracking_Vote_Count.png">
</p>

After making these changes, we also needed to loop through the counties from the dictionary to retrieve the county vote count, calaculate the percentage per county, and print the county results. We also added in a few extra lines that added these results to a text file. All of this ended, with us writing an IF statement that printed the correct county as the "Largest County Turnout" variable. 

 <p align="center">
  <img width="400" height="600" src="https://github.com/jcarter211/election-analysis/blob/main/Supporting%20Materials/Looping_through_counties.png">
</p>

 ## Challenge Summary 
 
