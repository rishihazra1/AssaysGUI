# reads stored csv (user-editable) with baseline data 
# calculates calculated excel columns 
# sends to bradford_assay.py for linear regression 
# convention: volume BSA, volume water, total volume, concentration BSA, Abs. 1, Abs. 2, Abs. avg;
# all numbers/positions come from example spreadsheet bradford 7.11.21
import csv
from os import system, path
import tkinter as tk
from tkinter import filedialog 
import datetime
import shutil
import grid_based_GUI as gui

fields = ['1 mg/mL BSA (µL)', 'H2O (µL)', 'BSA (mg/mL)', 'A_562 (1)', 'A_562 (2)']  
#calculated_fields = ['Total volume (µL)', 'A_562 (avg)']  #calculated fields: 'Total volume (µL)',  'A_562 (avg.)'
baselines = [['20', '0', '1.000', '1.258', '1.155'], ['15', '5', '0.750', '1.083', '1.098'], ['10', '10', '0.500', '0.728', '0.713'], ['5', '15', '0.250', '0.422', '0.402'], ['2.5', '17.5', '0.125', '0.223', '0.214'], ['0', '20', '0.000', '0', '-0.005']]  # eventually remove quotes, to make them of type float
master_baseline_file_name = 'standard_assay_master_baseline.csv'
default_baseline_file_name = 'standard_assay_default_baseline.csv'
last_saved_file_name = 'standard_assay_last_saved.csv'

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

def override_default_baseline():
    shutil.copyfile(last_saved_file_name, default_baseline_file_name)
    return

def restore_default_baseline(message_text):
    shutil.copyfile(master_baseline_file_name, default_baseline_file_name)
    message_text.configure(text="Default baseline restored from master baseline") 
    return

def create_master_baseline():
    if path.isfile(master_baseline_file_name) == False:
        with open(master_baseline_file_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for row in baselines:
                csvwriter.writerow(row)
        shutil.copyfile(master_baseline_file_name, default_baseline_file_name)
        shutil.copyfile(master_baseline_file_name, last_saved_file_name)
    return

def save_modified_baseline(table, message_text):
    #file_name = filedialog.asksaveasfilename(title='Enter file name',defaultextension='.csv', initialfile='standard_assay_'+ datetime.datetime.now().strftime('%m.%d.%Y.%H.%M.%S'))
    #directory_location = filedialog.askdirectory(title='Select  directory location')
    #file_name = 'standard_assay_'+ datetime.datetime.now().strftime('%m.%d.%Y.%H.%M.%S') + '.csv'
    message_text.configure(text="") 
    with open(last_saved_file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        rowNumber=0
        for row in table:
            if (rowNumber != 0):
                for data in row:
                    try:
                        float(data)
                    except ValueError:
                        message_text.configure(text="Invalid data entered. Enter valid number") 
                        return
            csvwriter.writerow(row)
            rowNumber+=1
    #shutil.copyfile(last_saved_file_name, file_name)
    message_text.configure(text="File saved") 
    return 

def read_stored_baseline(file_name,message_text):
    message_text.configure(text="") 
    #file_name = filedialog.askopenfilename(title="Select file", filetypes=(("CSV Files", "*.csv*"), ("All Files", "*.*")))
    table = []
    with open(file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            table.append(row)
    return table

def read_stored_baseline_without_header(file_name):
    table = []
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
