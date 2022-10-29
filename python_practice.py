counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver' :
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not in the list of countries.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Araphoe and El Paso are in the list of counties")
else:
    print("Araphaoe and El Paso is not in list.")
for county in counties:
    print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.") 
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + "{:,}".format(voters) + " registered voters.")