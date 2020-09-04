import os
import csv

profit_losses = 0
months = []
avg_change = []
profit_change =[]

path = os.path.join("Resources", "budget_data.csv")
Output_Path = os.path.join("Analysis", "Analysis.txt")

with open(path, "r") as file:
    csv_reader = csv.DictReader(file)
    next(csv_reader)
    
    for row in csv_reader:
        months.append(str(row[0]))
        profit_losses.append(int(row[1]))

for i in range(1, len(profit_losses)):
    profit_change.append(int(profit_losses[i]) - int(profit_losses[i-1]))
    
avg_change = sum(profit_change)/len(profit_change)


total_months = len(months)
total_amount = sum(profit_losses)
greatest_increase_index = months[profit_change.index(greatest_increase) +1]
greatest_decrease_index = months[profit_change.index(greatest_decrease)+1] 

output =(
f"total months:{total_months}\n"
f"Total amount: ${total_amount}\n"
f"Average Change: ${str(round(avg_change,2))}\n"
f"Greatest Increase in Profits: {greatest_increase_index} ${greatest_increase}\n"
f"Greatest Decrease in Profits: {greatest_decrease_index} (${greatest_decrease})\n")

print(output)

with open(Out_Path, "w") as txt_file:
    txt_file.write(output) 

