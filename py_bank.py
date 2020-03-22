import os 
import csv

budget_data_csv = os.path.join("data","budget_data.csv")

month_count=0
profit_loss=0
Average_Change=0
Daily_Change_List=[]
Previous_Profit_Loss=0
month_change=[]
Greatest_Increase=["",0]
Greatest_Decrease=["",999999999999]

#opening and reading the csv file 
with open (budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read the header row
    csv_header=next(csvreader)
    print(f"Header: {csv_header}")

    secondrow=next(csvreader)
    Previous_Profit_Loss= int(secondrow[1]) 
    profit_loss+= int(secondrow[1])

    month_count+=1


    #calculate the total number of months included in the data set
    for row in csvreader:
        month_count+=1
        profit_loss+=int (row[1])
        #track the net change 
        net_change=int(row[1])-Previous_Profit_Loss
        Previous_Profit_Loss=int (row[1])
        Daily_Change_List=Daily_Change_List+[net_change]
        if net_change > Greatest_Increase[1]:
            Greatest_Increase[0]=row[0]
            Greatest_Increase[1]=net_change
        if net_change < Greatest_Decrease[1]:
            Greatest_Decrease[0]=row[0]
            Greatest_Decrease[1]=net_change
Average_Change=sum(Daily_Change_List)/len(Daily_Change_List)
print(month_count) 
print(profit_loss)  
print(Average_Change)
print(Greatest_Increase[0],Greatest_Increase[1])
print(Greatest_Decrease[0],Greatest_Decrease[1])





    


    





