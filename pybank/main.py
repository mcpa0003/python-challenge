import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="")as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   # print(csv_header)


    total = 0
    months = 0
    Profit_List = []
    Profit_Change_List = []
    Profit_Gain_List = []
    Profit_Reduce_List = []

    for row in csvreader:

        months = months + 1
        profit = int(row[1])
        total = total + profit
        if months != 1:
            if last_month > profit:
                change = last_month - profit
                neg_change = (change) * -1
            
                Profit_Change_List.append(row[0])
                Profit_Change_List.append(neg_change)
                Profit_Reduce_List.append(neg_change)

            else:
                change = profit - last_month
                Profit_Change_List.append(row[0])
                Profit_Change_List.append(change)
                Profit_Gain_List.append(change)
            


        
        Profit_List.append(profit)
        last_month = profit
      
Maximum = max(Profit_Gain_List)
Minimum = min(Profit_Reduce_List)
#print("hello")

print("Financial Analysis \n ..................... \nTotal Months: \n" + str(months) + "\n  \ntotal: \n" + str(total) + "\n \nLargest increase in profits: \n" +str(Maximum) + "\n\nGreatest decrease in profits: \n" + str(Minimum))





output_path = os.path.join("Output", "PybankOutput.txt")
with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow("Financial Analysis \n ..................... \nTotal Months: \n" + str(months) + "\n  \ntotal: \n" + str(total) + "\n \nLargest increase in profits: \n" +str(Maximum) + "\n\nGreatest decrease in profits: \n" + str(Minimum))







        

    












 
































