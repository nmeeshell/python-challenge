import os
import csv
import sys

sum_profits = 0
months = []
changes = []
greatest_change = []
negative_change = []
count = 0

in_path = os.path.join("Resources", "budget_data.csv")
Output_Path = os.path.join("Analysis", "Analysis.txt")

with open(in_path, "r") as file:
    print("file: ", file)
    reader = csv.DictReader(file)
    print("reader: ",reader)
    
    for row in reader:
        print(50 * "=")
        print ("type(row): ",type(row))
        print("row: ", row)
        row_dict = dict(row)
        print("row_dict: ", row_dict)
        profit = row_dict["Profit/Losses"]
        print("profit: ", profit)
        print("type(profit): ", type(profit))
        profit_float = float(profit)
        print("profit_float: ", profit_float)
        sum_profits += profit_float
        print("sum_profits:", sum_profits)
        count +=1
        print ("count: ", count)
        
        
print(50 * "=")
print("sum_profits: ", sum_profits)
print(changes)
print(months)

avg_profits = sum_profits / count
print("avg_profits: ", avg_profits)
greatest_change = int(input(changes)).max
greatest_month = months[changes.index(greatest_change) +1] 
negative_change = int(input(changes)).min
negative_month = months[changes.index(negative_change) +1]

output =(
(f"Financial Analysis\n")
(f"------------------\n")
(f"Total months:{num_months}\n")
(f"Total profit loss: ${total_profit_loss:,.2f}\n")
(f"Average Change: ${avg_profits}")
(f"Greatest Increase in Profits: {greatest_month} (${greatest_change:,.2f})\n")
(f"Greatest Decrease in Profits: {negative_month} (${negative_change:,.2f})\n")
)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output) 

