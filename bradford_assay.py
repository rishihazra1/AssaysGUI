import bradford_baseline as baseline
import data_analysis as da
import input_validation 
import simple_statistics
import math
import tkinter as tk

def bradford_assay_main(master, protein_used, dilution, absorption, stored_baseline_result_text, default_baseline_result_text, default_selected, doPlot):
    try:
        protein_used = float(protein_used)
    except ValueError:
        print("ERROR -- protein_amount")
        stored_baseline_result_text.configure(text="Invalid protein amount entered. Try again.")
        default_baseline_result_text.configure(text='')
    
    try:
        dilution = float(dilution)
    except ValueError:
        print("ERROR -- dilution")
        stored_baseline_result_text.configure(text="Invalid dilution entered. Try again.")    
        default_baseline_result_text.configure(text='')    
    
    try:   
        absorption = float(absorption)
    except ValueError:
        print("ERROR -- absorption")
        stored_baseline_result_text.configure(text="Invalid absorption. Try again.") 
        default_baseline_result_text.configure(text='')

    dilution_factor = (protein_used/20)*dilution

    #default baseline
    if (default_selected == 1):
        x_terms_1, y_terms_1 = calculate_baselines(baseline.read_stored_baseline_without_header(baseline.default_baseline_file_name))
        display_stats(x_terms_1, y_terms_1, absorption, dilution_factor, default_baseline_result_text, "Default Baseline:")
    else:
        default_baseline_result_text.configure(text='')
   
    #last saved baseline
    x_terms_2, y_terms_2 = calculate_baselines(baseline.read_stored_baseline_without_header(baseline.last_saved_file_name))
    display_stats(x_terms_2, y_terms_2, absorption, dilution_factor, stored_baseline_result_text, "Last Saved Baseline:")

    if(doPlot ==1):
        if (default_selected ==1):
            da.plot_from_2_arrays(x_terms_1, y_terms_1, x_terms_2, y_terms_2)
        else:
            da.plot_from_arrays(x_terms_2, y_terms_2)


def display_stats(x_terms, y_terms, absorption, dilution_factor, output_text, baselineText):
    a, b, c = simple_statistics.get_best_fit_line(x_terms, y_terms)  # values generated through numpy polyfit
    r_squared = simple_statistics.get_r_squared(x_terms, y_terms, a, b, c)
    concentration = ((-b + math.sqrt(b**2 - 4*a*c + 4*a*float(absorption)))/(2*a))/dilution_factor
    output_text.configure(text=baselineText + '\n' + str(round(absorption,4)) + "A →  " + str(round(concentration,4))+ " mg/mL\n" + "r² = " + str(round(r_squared,4)))     
    

baseline_values = [[]]
def calculate_baselines(baseline_values):
    y_average_absorption = []
    x_BSA_concentration = []
    for i in range(0, len(baseline_values)):
        temp_average = (float(baseline_values[i][3]) + float(baseline_values[i][4]))/2  
        y_average_absorption.append(temp_average)
        x_BSA_concentration.append(float(baseline_values[i][2]))
    return x_BSA_concentration, y_average_absorption
