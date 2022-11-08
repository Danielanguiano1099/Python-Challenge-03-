import os
import csv

#Print "Election Results"
print(" Election Results", "\n","\n","------------------------","\n")


#Print "-----------------------"

#Write code that coutns all votes, might need to use the length of total counts

csvpath = os.path.join("Resources", "election_data.csv")

Count = []
Charles = []
Diana = []
Raymon = []





with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        counts = row[0]
        Count.append(counts)
        if row[2] == "Charles Casper Stockham":
            Charles_count = row[2]
            Charles.append(Charles_count)
        elif row[2] == "Diana DeGette":
            Diana_count = row[2]
            Diana.append(Diana_count)
        elif row[2] == "Raymon Anthony Doane":
            Raymon_count = row[2]
            Raymon.append(Raymon_count)
    if len(Raymon) > (len(Charles) and len(Diana)):
        winner = str("Raymon Anthony Doane")
    if len(Charles) > (len(Raymon) and len(Diana)):
        winner = str("Charles Casper Stockham")
    if len(Diana) > (len(Charles) and len(Raymon)):
        winner = str("Diana DeGette")

        












print(" Total Votes: " + str(int(len(Count) -1)) + "\n" + "\n" 
+ " ----------------------" + "\n" + "\n")


print(" Charles Casper Stockham: " + str(format((int(len(Charles))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Charles))) + ")" +"\n")
print(" Diana DeGette: " + str(format((int(len(Diana))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Diana))) + ")" +"\n" )
print(" Raymon Anthony Doane: " + str(format((int(len(Raymon))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Raymon))) + ")" + "\n")
print(" --------------------" + "\n", "\n" + " Winner: " + str(winner) + "\n", "\n" + " ------------------------" + "\n")

a = " Total Votes: " + str(int(len(Count) -1)) + "\n" + "\n" + " ----------------------" + "\n" + "\n"
b = " Charles Casper Stockham: " + str(format((int(len(Charles))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Charles))) + ")" +"\n" + "\n"
c = " Diana DeGette: " + str(format((int(len(Diana))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Diana))) + ")" +"\n" +"\n" 
d = " Raymon Anthony Doane: " + str(format((int(len(Raymon))/int(len(Count) -1))*100,'.3f') + "% ") + "(" + str(int(len(Raymon))) + ")" + "\n" +"\n"
e = " --------------------" + "\n" + "\n" + " Winner: " + str(winner) + "\n"+ "\n" + " ------------------------" + "\n"
f =" Election Results"+ "\n"+"\n"+"------------------------"+"\n"+"\n"
txt = os.path.join("Analysis")
with open("Analysis/PYTHON_ANALYSIS-PYPOLL", "w") as file:
    lines = ([f,a,b,c,d,e])
    file.writelines(lines)

