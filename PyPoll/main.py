import os
import csv
import sys

in_path = os.path.join("Resources" , "election_data.csv")
out_path = os.path.join("Analysis", "analysis.txt")

Voter_ID = []
County = []
Khan =[]
Correy =[]
Li = []
OTooley = []
votes = [] 
candidate =[1,2] 
candidates =["Khan","Correy","Li","O'Tooley"]
row_count = [] 

with open(in_path, "r") as file:
    csv_reader=csv.reader(file)
    
data = [
    ["Khan", 2218231],
    ["Correy", 704200],
    ["Li", 492940],
    ["O_Tooley", 105630]
]
results = {}

for candidate, votes in data:
    if candidate in results:
        results[candidate] += votes
    else:
        results[candidate] = votes
    
    print(50  * "=")
    print(results)

    percent_votes = votes / votes * 100
    print(f"{row_count}: {percent_votes:,.3f}% ({votes:,.0f})) 
    print(divider)
    print(f"Winner: {winner}")
    print(divider)


with open(out_path, "w") as txt_file:
    txt_file.write(out_path) 
     

