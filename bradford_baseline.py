# reads stored csv (user-editable) with baseline data 
# calculates calculated excel columns 
# sends to bradford_assay.py for linear regression 
# convention: volume BSA, volume water, total volume, concentration BSA, Abs. 1, Abs. 2, Abs. avg;
# all numbers/positions come from example spreadsheet bradford 7.11.21
import csv
import tkinter as tk

fields = ['1 mg/mL BSA (µL)', 'H2O (µL)', 'BSA (mg/mL)', 'A_562 (1)', 'A_562 (2)']  
#calculated_fields = ['Total volume (µL)', 'A_562 (avg)']  #calculated fields: 'Total volume (µL)',  'A_562 (avg.)'
baselines = [['20', '0', '1.000', '1.258', '1.155'], ['15', '5', '0.750', '1.083', '1.098'], ['10', '10', '0.500', '0.728', '0.713'], ['5', '15', '0.250', '0.422', '0.402'], ['2.5', '17.5', '0.125', '0.223', '0.214'], ['0', '20', '0.000', '0', '-0.005']]  # eventually remove quotes, to make them of type float
     
def get_baseline_fields():
    return fields

def get_default_baseline_values():
    return baselines

def get_default_baseline():
    table = []
    table.append(fields)
    for row in baselines:
        table.append(row)
    return table

def save_modified_baseline(table):
    file_name = "standard_assay.csv" 
    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in table:
            csvwriter.writerow(row)
    print("Stored at " + str(file_name))
    return file_name 

def read_stored_baseline():
    table = []
    file_name = "standard_assay.csv" 
    with open(file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            table.append(row)
    return table

def read_stored_baseline_without_header():
    table = []
    file_name = "standard_assay.csv" 
    with open(file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            table.append(row)
    
    newTable =[]
    rowNumber=0
    for rows in table:
        if (rowNumber !=0):
            newTable.append(rows)
        rowNumber+=1
    
    return newTable

baseline_values = [[]]
def calculate_baselines(baseline_values):
    y_average_absorption = []
    x_BSA_concentration = []
    for i in range(0, len(baseline_values)):
        temp_average = (float(baseline_values[i][3]) + float(baseline_values[i][4]))/2  
        y_average_absorption.append(temp_average)
        x_BSA_concentration.append(float(baseline_values[i][2]))
    
    return x_BSA_concentration, y_average_absorption