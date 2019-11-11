# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:19:53 2019

@author: lhern
"""

# Import File
import os
import csv

file_num = 2
# Open CSV file 
file = os.path.join("C:/Users/lhern/Documents/Python Original/Python Homework/PyBank/Resources/budget_data.csv")

#how to read file
with open(file, newline='') as csvfile:
# CSV reader specifies delimiter and variable that holds contents    
    csvreader = csv.reader(csvfile, delimiter=",")  

#emply lists for month and revenue data
months = []
revenue = []

#read csv and parse data into lists
#revenue list will be list of integers
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#find total months
total_months = len(months)
total_revenue += int(revenue[1])

#create greatest increase, decrease variables and set them equal to the first revenue entry
#set total revenue = 0 
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#loop through revenue indices and compare # to find greatest inc and dec
#also add each revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
        total_revenue += revenue[r]

#calculate average_change
average_change = round(total_revenue/total_months, 2)

#sets path for output file
output_dest = os.path.join('Output','pybank_output_' + str(file_num) + '.txt')
output_dest = os.path.join("C:/Users/lhern/Documents/Python Original/Python Homework/PyBank/main.py/PyBank")

# opens the output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())