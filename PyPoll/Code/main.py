import os
import csv
import collections


# path to collect data from resources folder
poll_csv = os.path.join('../Resources','election_data.csv')


candidates = collections.Counter()

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    
    # Total number of votes cast
    totalVotes = sum(1 for line in open(poll_csv)) - 1

    #print(totalVotes)


    #-----------
    # A complete list of candidates who received votes

    candidateList = []
    for row in csvreader:
        candidates[row[2]] +=1
        if row[2] not in candidateList:
            candidateList.append(row[2])

    # print(candidateList)


    #-------------
    # The percentage of votes each candidate won
    
  
    


    # The total number of votes each candidate won
    winner_value=max(candidates.values())
    winner=[k for k,v in candidates.items() if v==winner_value] 

    
    
    print("```")
    print("Election Results")
    print("-----------------------------")
    print("Total Votes:", "{:,}".format(totalVotes))
    print("-----------------------------")
    for key, value in candidates.items():
        print(key, ":", "{:.1%}".format(value / totalVotes), f'({"{:,}".format(value)})')
    print("-----------------------------")
    print("Winner:",winner)
    print("-----------------------------")


     # Output

    output_path = os.path.join("PyPoll_Output.csv")

    with open (output_path,'w',newline='') as csvfile:
    
        #initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        csvwriter.writerow(["```"])
        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["-----------------------------"])
        csvwriter.writerow(["Total Votes:", "{:,}".format(totalVotes)])
        csvwriter.writerow(["-----------------------------"])
        for key, value in candidates.items():
            csvwriter.writerow([f'{key}:', "{:.1%}".format(value / totalVotes), f'({"{:,}".format(value)})'])
        csvwriter.writerow(["-----------------------------"])
        csvwriter.writerow(["Winner:",winner])
        csvwriter.writerow(["-----------------------------"])