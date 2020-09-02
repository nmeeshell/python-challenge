import os
import csv

#OUT_PATH = "budget_data.csv"

path = os.path.join("Resources" , "budget_data.csv")

Months = []
Profit_Losses = []
Avg_Change = []
Profit_Change = [] 

with open(path,"r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        Months.append(str(row[0]))
        Profit_Losses.append(int(row[1])) 
    
for i in range(1, len(Profit_Losses)):
    Profit_Change.append((int(Profit_Losses[i]) - int(Profit_Losses[i-1])))
        
Avg_Change = sum(Profit_Change)/len(Profit_Change) 
    

total_months = len(Months)
total_amount = sum(Profit_Losses)


print(f" Total Months: {total_months}")
print(f" Total Amount: ${total_amount}") 
print(f" Average Change: ${str(round(Avg_Change,2))}")  
print(f" Greatest Increase in Profits: ${max(Profit_Losses)}") 
print(f" Greatest Decrease in Profits: ${min(Profit_Losses)}") 



# Greatest_Increase =
# Greatest_decrease = 
    
    # with open (OUT_PATH, "w+") as file:
    
#     # csv_writer = csv.DictWriter(file, 
#                                [ "Profits" ,
#                                  "Losses" ,
#                                  "Months" ,
#                                  "Years"])
    
#     #for row in data:
        
#         row = dict(row)
        
#         profits = int(row["Profits"])
#         losses = int(row ["Losses"])
#         date = int(row ["Date"])
#         date = (row ["Date"])
        
#         total_number = profits + losses
#         row["profits/losses"] = wins + losses / total_number
        
#        csv_writer.writerow(row)
        
        
        