#Import all programs needed to run this code ie : os and csv
import os
import csv

# print the analysis name and seperating border for the analysis

print("Financial Analysis")
print(" ")
print("---------------------------------")
#Import csv using os.path
csvpath = os.path.join("Resources", "budget_data.csv")
#create lists for total votes, and total votes for each candidate
# create varibales to track total proft, average change month to month, greatest increase
# and greatest decrease
Months=[]
Total = 0
Change = 0
Avgchge = 0
increase = 0
decrease = 0
#open csv as a csv file and make sure header matches data style
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#append vote count to count list
# track total net for the year 
    for row in csvreader:
        month = row[0]
        Months.append(month)
        profit = int(row[1])
        Total = Total + profit
        # create a code that does not account for the header to track change month 
        # to month so we can then find average change
        if row[1] != 0:

            Change = Change + int(row[1])
            # write if statement to track greatest increase as well as greatest decrease
            if int(Change) > increase:
                increase = int(Change)
                day = str(row [0])
            
            if int(Change) < decrease:
                decrease = int(Change)
                days = str(row[0])
                
            Avgchge = Avgchge + Change
            Change = -int(row[1])
        
    #write code that counts total month using len function     
    print("Total Months: " + str(int(len(Months) -1)))
    print(" ")
    # write print statements that displays all results in Anlaysis Results
    print("Total: $" + str(int(Total)) )
    print(" ")
    print("Average Change: $" + str(format(float((Avgchge - 1088983)/(int(len(Months))-2)), '.2f')))
    print(" ")
    print("Greatest Increase in Profits: " + str(day) + " ($" + str(increase) +")")
    print(" ")
    print("Greatest Decrease in Profits: " + str(days) + " ($" + str(decrease) +")")
    

   #declare variables to include as outputs for file export
    aa = " Financial Analysis"
    bb = "\n "
    ab = "\n "
    cc = "---------------------------------"
    bc = "\n "
    a = "Total Months: " + str(int(len(Months) -1))
    b = "\n "
    ba= "\n "
    c = "Total: $" + str(int(Total))
    d = "\n"
    dc= "\n "
    e = "Average Change: $" + str(format(float((Avgchge - 1088983)/(int(len(Months))-2)), '.2f'))
    f = "\n"
    fe ="\n "
    g = "Greatest Increase in Profits: " + str(day) + " ($" + str(increase) +")"
    h = " \n"
    hg = "\n "
    i = "Greatest Decrease in Profits: " + str(days) + " ($" + str(decrease) +")"
    
    # write a with statement to add file to Analysis folder named: "PYTHON_ANALYSIS"
    with open( "Analysis/PYTHON_ANALYSIS.txt", "w") as file:
        # Now that we have variables, assign them to a list and 
        # then use 'writelines' to write these results
        lines = ([aa,bb,ab,cc,bc,a,b,ba,c,d,dc,e,f,fe,g,h,hg,i])
        file.writelines(lines)


        


        

        






     


        




        





    
       














