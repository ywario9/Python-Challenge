import os

#import module to read CSV files
import csv


csvpath=os.path.join('data','election_data.csv')


#read csv module
candidate_vote={}
candidate_option=[]
total_vote=0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    #read the header row first 
    headerrow=next(csvreader,None)

    #set variables

   
    
    for row in csvreader:
        candidate_name=row[2]

        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            candidate_vote[candidate_name]=0

        candidate_vote[candidate_name]=candidate_vote[candidate_name]+1

total_vote=sum(candidate_vote.values())

percentage=[]

print ("Election Results")
print ("---------------------")
output=(
    f'\nElection Results\n'
    f'-----------------------\n'

    f'Total Votes: {total_vote}'
    f'-------------------')

    #percent of vote per candidate

for candidate in candidate_vote:
    percentage=((candidate_vote[candidate]/total_vote)*100)

print(output)


