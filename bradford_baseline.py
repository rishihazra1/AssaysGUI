# reads stored csv (user-editable) with baseline data 
# calculates calculated excel columns 
# sends to bradford_assay.py for linear regression 
# convention: volume BSA, volume water, total volume, concentration BSA, Abs. 1, Abs. 2, Abs. avg;
# all numbers/positions come from example spreadsheet bradford 7.11.21
import csv
import tkinter as tk

fields = ['1 mg/mL BSA (µL)', 'H2O (µL)', 'BSA (mg/mL)', 'A_562 (1)', 'A_562 (2)']  
calculated_fields = ['Total volume (µL)', 'A_562 (avg)']  #calculated fields: 'Total volume (µL)',  'A_562 (avg.)'
baselines = [['20', '0', '1.000', '1.258', '1.155'], ['15', '5', '0.750', '1.083', '1.098'], ['10', '10', '0.500', '0.728', '0.713'], ['5', '15', '0.250', '0.422', '0.402'], ['2.5', '17.5', '0.125', '0.223', '0.214'], ['0', '20', '0.000', '0', '-0.005']]  # eventually remove quotes, to make them of type float
     
def get_baseline_fields():
    return fields

def get_calculated_baseline_fields():
    return calculated_fields

def get_default_baseline_values():
    return baselines

def save_modified_baseline(rows):
    
    file_name = "standard_assay.csv" 
    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(rows)
    print("Stored at " + str(file_name) + " Ctrl + Click to open.")
    return file_name 

def read_stored_baseline():
    baseline_values = [[]]
    file_name = "standard_assay.csv" 
    with open(file_name, 'r') as csvfile:
        baseline_values = csv.reader(csvfile)
    return baseline_values
