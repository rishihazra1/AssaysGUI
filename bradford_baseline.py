# reads stored csv (user-editable) with baseline data 
# calculates calculated excel columns 
# sends to bradford_assay.py for linear regression 
# convention: volume BSA, volume water, total volume, concentration BSA, Abs. 1, Abs. 2, Abs. avg;
# all numbers/positions come from example spreadsheet bradford 7.11.21
import csv

def set_default_baseline():
    fields = ['1 mg/mL BSA (µL)', 'H2O (µL)', 'BSA (mg/mL)', 'A_562 (1)', 'A_562 (2)']  #calculated fields: 'Total volume (µL)',  'A_562 (avg.)'
    rows =  [['20', '0', '1.000', '1.258', '1.155'], ['15', '5', '0.750', '1.083', '1.098'], ['10', '10', '0.500', '0.728', '0.713'], ['5', '15', '0.250', '0.422', '0.402'], ['2.5', '17.5', '0.125', '0.223', '0.214'], ['0', '20', '0.000', '0', '-0.005']]  # eventually remove quotes...
    file_name = "standard_assay.csv" 
    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(rows)
    print("Stored at " + str(file_name) + " Ctrl + Click to open.")
    return file_name 

def get_baselines():
    baselines = [['20', '0', '1.000', '1.258', '1.155'], ['15', '5', '0.750', '1.083', '1.098'], ['10', '10', '0.500', '0.728', '0.713'], ['5', '15', '0.250', '0.422', '0.402'], ['2.5', '17.5', '0.125', '0.223', '0.214'], ['0', '20', '0.000', '0', '-0.005']]  # eventually remove quotes, to make them of type float
    return baselines


baseline_values = [[]]
y_average_absorption = []
x_BSA_concentration = []
def calculate_baselines(baseline_values):
    for i in range(0, len(baseline_values)):
        temp_average = (float(baseline_values[i][3]) + float(baseline_values[i][4]))/2  
        y_average_absorption.append(temp_average)
        x_BSA_concentration.append(float(baseline_values[i][2]))
    return x_BSA_concentration, y_average_absorption