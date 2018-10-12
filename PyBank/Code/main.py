import os
import csv
import locale
locale.setlocale(locale.LC_ALL, '')

# path to collect data from resources folder
budget_csv = os.path.join('../Resources','budget_data.csv')





with open(budget_csv, 'r') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',')

        #skips the header row
        header = next(csvreader)
        
        # Number of months
        NumberOfMonths = sum(1 for line in open(budget_csv))-1
        #print("Number of Months:",NumberOfMonths)
            

        # total profit Loss
        totalProfitLoss2 = 0
       
        months = []
        values = []
        difference = []
        num = 0
        for row in csvreader:
            totalProfitLoss2 += int(row[1])

            values.append(int(row[1]))
            months.append(row[0])

            num2 = int(row[1])
            num3=(num2 - num)
            difference.append(num3)
            num = int(row[1])
            
        difference.pop(0)
    
        totalProfitLoss = locale.currency(totalProfitLoss2,grouping=True)
        largestGain = locale.currency(max(values),grouping=True)
        largestGainMonth = months[values.index(max(values))]
        largestLoss = locale.currency(min(values),grouping=True)
        largestLossMonth = months[values.index(min(values))]
        averageChange = locale.currency(sum(difference)/(len(difference)),grouping=True)
        
    
        print("```")
        print("Financial Analysis")
        print("-----------------------------------------------")
        print("Total  Months:", NumberOfMonths)
        print("Total: $", totalProfitLoss)
        print("Average Change: $", averageChange)
        print("Greatest Increase in Profits:", largestGainMonth, f'({largestGain})')
        print("Greatest Decrease in Profits:", largestLossMonth, f'({largestLoss})')

        output_path = os.path.join("PyBank.csv")

        with open (output_path,'w',newline='') as csvfile:

             #initialize csv.writer
            csvwriter = csv.writer(csvfile, delimiter=',')

            csvwriter.writerow(["```"])
            csvwriter.writerow(["Financial Analysis"])
            csvwriter.writerow(["-----------------------------------------------"])
            csvwriter.writerow(["Total  Months:", NumberOfMonths])
            csvwriter.writerow(["Total: $", totalProfitLoss])
            csvwriter.writerow(["Average Change: $", averageChange])
            csvwriter.writerow(["Greatest Increase in Profits:", largestGainMonth, f'({largestGain})'])
            csvwriter.writerow(["Greatest Decrease in Profits:", largestLossMonth, f'({largestLoss})'])



