counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.") 

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes_C = 0
total_votes_D = 0
total_votes_R = 0
# Candidate options and candidate votes
#candidate_options = []
# 1. Declare the empty dictionary.
#candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
for row in file_reader:
     if candidate_name = "Charles Casper Stockham":
         total_votes_C += 1
     elif candidate_name = "Diana DeGette":
         total_votes_D += 1 
     else candidate_name = "Raymon Anthony Doane":
         total_votes_R += 1 
print(total_votes_c,total_votes_D,total_votes_R)

name =" Joe"
country = " USA"
age = 35
hourly_wage = 70
satisfied = True
daily_wage = hourly_wage*8
print(f"hello {name}")
print(f" I live in {country}")
print(f" I earn {daily_wage}")
print(f" are you satisfied with your salary?{satisfied}")

List= ['Milk','Bread','Eggs','Peanut Butter','Jelly' ]
print(List)
List[3]= 'Almond Butter'
List.remove('Jelly')
List.append('coffee')
print(List)


Nazanin_Dictionary = { 'name': "Nazanin", 'age':"31" ,'hobbies':["running" ,"playing Piano"]
Nazanin_Dictionary2 = {'times':["9.00","8:00"]}

print(Nazanin_Dictionary)












