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
Total_Votes = [] 
candidate =[1,2] 
Candidates =["Khan","Correy","Li","O'Tooley"]
row_count = [] 

with open(in_path,"r") as file:
    csv_reader = csv.reader(file) 
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        if candidate[0] == row[1]:
            Khan +=1
        if candidate [0] ==row[1]:
            Correy +=1
        if candidate[0] ==row[1]:
            Li +=1
        if candidate[0] ==row[1]:
            OTooley +=1 
    

def print_results(Total_Votes, Candidates):
    divider = "-" * 25
    print("Election Results")
    print(divider)
    print(f"Total votes: {Total_Votes:,.0f}")
    print(divider)

    most_votes = 0

    for row in candidates:
        
    
        votes = Candidates[row]
        percent_votes = votes / Total_Votes * 100
        print(f"{row}: {percent_votes:,.3f}% ({votes:,.0f})")
        
      
        if Candidates[row] > most_votes:
            most_votes = Candidates[row]
            winner = row
 

  
    print(divider)
    print(f"Winner: {winner}")
    print(divider)
        
print_results(Total_Votes, Candidates)
 
Output_Path_Variable= "analysis/results.text"

with open(Output_Path_Variable, "w") as txt_file:
        txt_file.write(Print_Statements_in_Variable)
     

