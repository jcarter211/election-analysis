# Election Analysis 

## Project Overview 
A Colorado Board of Elections employee has asked for me to help him assess the results of a U.S. congressional precinct in Colorado. There are a few different election results that Tom, the elections employees, would like to find in particular: 
  * The total number of notes for each candidate 
  * The percentage of votes for each candidate 
  * The winner of the election based on the popular vote 
In the past, the elections committee has used Excel. They would like for Tom and I to create a more automated process by using Python and creating code that they may use in all future elections. 
After receiving the intitial data, the election commission requested a few more pieces of information. 
  * The voter turnout for each county
  * The percentage of votes from each county out of the total vote count
  * The country with the highest turnout
  
## Challenge Results 
  <p align="center">
  <img width="400" height="600" src="https://github.com/jcarter211/election-analysis/blob/main/Supporting%20Materials/Election_Results.png">
</p>

The results of the election are seen above. 
  * There were 369,711 votes cast in the election. 
  * The couny results were:
    * Jefferson received 10.5% of the votes (38,855).
    * Denver received 82.8% of the votes (306, 055. 
    * Arapahoe received 6.7% of the votes (24,801). 
  * Denver had the largest county turnout. 
  * The candidate results were:
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606) 
  * The winner of the elction was: 
    * Diana DeGette, who received 73.8% of the popular vote and 272,892 number of votes.
 
In order to add the county to our election audit, we needed to add code that supported the information about each county. To begin, we first had to identify a new list and dictionary: election_counties, county_votes. We then needed to add the counties to the election_counties list and add the updated list to the dictionary. Once the counties were added to the dictionary, we began to track and add votes to the county's vote count. 
 
 <p align="center">
  <img width="500" height="500" src="https://github.com/jcarter211/election-analysis/blob/main/Supporting%20Materials/Tracking_Vote_Count.png">
</p>

After making these changes, we also needed to loop through the counties from the dictionary to retrieve the county vote count, calaculate the percentage per county, and print the county results. We also added in a few extra lines that added these results to a text file. All of this ended, with us writing an IF statement that printed the correct county as the "Largest County Turnout" variable. 

 <p align="center">
  <img width="500" height="500" src="https://github.com/jcarter211/election-analysis/blob/main/Supporting%20Materials/Looping_through_counties.png">
</p>

 ## Challenge Summary 
 It is my hope that the election commmission will use this script as a guide for all elections moving forward. I think that it will expedite the election audit process and provide information that better informs the commission of the election results. If the election board would like to continue using this script, there are a few modifications that would need to be made.
* The commission would need to upload a new csv file for each election so that the code is pulling from the correct election data. 
* To learn even more about the election, the commission could add in a few lines of code that would provide further information about many votes each candidiate received from each county. The commission could see if a certain county perferred one candidate over another.  
