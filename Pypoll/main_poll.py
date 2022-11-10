import csv
import os

#Print "Election Results"
print(" Election Results", "\n","\n","------------------------","\n")


#Wright "-----------------------"

#Import csv using os.path

csvpath = os.path.join("Resources", "election_data.csv")
#create lists for total votes, and total votes for each candidate
Count = []
Charles = []
Diana = []
Raymon = []
#open csv as a csv file and make sure header matches data style
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#append vote count to count list
    for row in csvreader:
        counts = row[0]
        Count.append(counts)
        # write if statement to append vote count to individual candidate lists
        if row[2] == "Charles Casper Stockham":
            Charles_count = row[2]
            Charles.append(Charles_count)
        
        elif row[2] == "Diana DeGette":
            Diana_count = row[2]
            Diana.append(Diana_count)
        
        elif row[2] == "Raymon Anthony Doane":
            Raymon_count = row[2]
            Raymon.append(Raymon_count)
    # write if statement to declare the winner of the election
    if len(Raymon) > (len(Charles) and len(Diana)):
        dinners = str("Raymon Anthony Doane")
    
    if len(Charles) > (len(Raymon) and len(Diana)):
        dinners = str("Charles Casper Stockham")
    
    if len(Diana) > (len(Charles) and len(Raymon)):
        dinners = str("Diana DeGette")
#Write code that coutns all votes, might need to use the length of total counts
print(" Total Votes: " + str(int(len(Count) -1)) + "\n" + "\n" 
+ " ----------------------" + "\n" + "\n")
print(" Charles Casper Stockham: " + str(format((int(len(Charles))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Charles))) + ")" +"\n")
print(" Diana DeGette: " + str(format((int(len(Diana))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Diana))) + ")" +"\n" )
print(" Raymon Anthony Doane: " + str(format((int(len(Raymon))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Raymon))) + ")" + "\n")
print(" --------------------" + "\n", "\n" + " Winner: " + str(dinners) + "\n", "\n" + " ------------------------" + "\n")
#declare variables to include as outputs for file export
a = " Total Votes: " + str(int(len(Count) -1)) + "\n" + "\n" + " ----------------------" + "\n" + "\n"
b = " Charles Casper Stockham: " + str(format((int(len(Charles))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Charles))) + ")" +"\n" + "\n"
c = " Diana DeGette: " + str(format((int(len(Diana))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Diana))) + ")" +"\n" +"\n" 
d = " Raymon Anthony Doane: " + str(format((int(len(Raymon))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Raymon))) + ")" + "\n" +"\n"
e = " --------------------" + "\n" + "\n" + " Winner: " + str(dinners) + "\n"+ "\n" + " ------------------------" + "\n"
f =" Election Results"+ "\n"+"\n"+"------------------------"+"\n"+"\n"
# write a with statement to add file to Analysis folder named: "PYTHON_ANALYSIS-PYPOLL"
txt = os.path.join("Analysis")
with open("Analysis/PYTHON_ANALYSIS-PYPOLL.txt", "w") as file:
    # Now that we have variables, assign them to a list and cd ..
    # then use 'writelines' to write these results
    lines = ([f,a,b,c,d,e])
    file.writelines(lines)

