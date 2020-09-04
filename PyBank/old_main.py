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
    next(csv_reader, None)
    
    for row in csv_reader:
        Months.append(str(row[0]))
        Profit_Losses.append(int(row[1])) 
    
for i in range(1, len(Profit_Losses)):
    Profit_Change.append((int(Profit_Losses[i]) - int(Profit_Losses[i-1])))

    
Avg_Change = sum(Profit_Change)/len(Profit_Change) 
    

total_months = len(Months)
total_amount = sum(Profit_Losses)
greatest_increase = round(max(Profit_Change),2)
greatest_decrease = round(min(Profit_Change),2)
greatest_increase_index = Profit_Change.index(greatest_increase) 
greatest_decrease_index = Profit_Change.index(greatest_decrease) 



print(f" Total Months: {total_months}")
print(f" Total Amount: ${total_amount}") 
print(f" Average Change: ${str(round(Avg_Change,2))}")  
print(f" Greatest Increase in Profits: {Months[greatest_increase_index +1]} ${max(Profit_Losses)}") 
print(f" Greatest Decrease in Profits: {Months[greatest_decrease_index +1]} ${min(Profit_Losses)}") 