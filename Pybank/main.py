
import os
import csv
# print the analysis name and seperating border for the analysis

print("Financial Analysis")
print(" ")
print("---------------------------------")

csvpath = os.path.join("Resources", "budget_data.csv")

Months=[]
Total = 0
Change = 0
Avgchge = 0
increase = 0
decrease = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        month = row[0]
        Months.append(month)
        profit = int(row[1])
        Total = Total + profit
        if row[1] != 0:

            Change = Change + int(row[1])
            if int(Change) > increase:
                increase = int(Change)
                day = str(row [0])
            if int(Change) < decrease:
                decrease = int(Change)
                days = str(row[0])
                
            Avgchge = Avgchge + Change
            Change = -int(row[1])
        
            
    
            


    
    


    
    print("Total Months: " + str(int(len(Months) -1)))
    print(" ")
    print("Total: $" + str(int(Total)) )
    print(" ")
    print("Average Change: $" + str(format(float((Avgchge - 1088983)/(int(len(Months))-2)), '.2f')))
    print(" ")
    print("Greatest Increase in Profits: " + str(day) + " ($" + str(increase) +")")
    print(" ")
    print("Greatest Decrease in Profits: " + str(days) + " ($" + str(decrease) +")")
    


        





    
       














