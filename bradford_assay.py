import bradford_baseline as baseline
import data_analysis as da
import input_validation 
import simple_statistics
import math
import tkinter as tk

def bradford_assay_main(master, protein_used, dilution, absorption, output_text_1, output_text_2):
    try:
        protein_used = float(protein_used)
    except ValueError:
        print("ERROR -- protein_amount")
        output_text_1.configure(text="Invalid protein amount entered. Try again.")
    try:
        dilution = float(dilution)
    except ValueError:
        print("ERROR -- dilution")
        output_text_1.configure(text="Invalid dilution entered. Try again.")        
    
    dilution_factor = (protein_used/20)*dilution

    #default baseline
    x_terms_1, y_terms_1 = baseline.calculate_baselines(baseline.read_stored_baseline_without_header(baseline.default_baseline_file_name))
    display_stats(x_terms_1, y_terms_1, absorption, dilution_factor, output_text_1, "Default Baseline")
   
    #last saved baseline
    x_terms_2, y_terms_2 = baseline.calculate_baselines(baseline.read_stored_baseline_without_header(baseline.last_saved_file_name))
    display_stats(x_terms_2, y_terms_2, absorption, dilution_factor, output_text_2, "Last Saved Baseline")

    da.plot_from_2_arrays(x_terms_1, y_terms_1, x_terms_2, y_terms_2)

def display_stats(x_terms, y_terms, absorption, dilution_factor, output_text, baselineText):
    a, b, c = simple_statistics.get_best_fit_line(x_terms, y_terms)  # values generated through numpy polyfit
    r_squared = simple_statistics.get_r_squared(x_terms, y_terms, a, b, c)
    try:   
        concentration = ((-b + math.sqrt(b**2 - 4*a*c + 4*a*float(absorption)))/(2*a))/dilution_factor
        output_text.configure(text=baselineText + str(absorption) + "A →  " + str(concentration) + " mg/mL\n" + "r² = " + str(r_squared))     
    except ValueError:
        print("ERROR -- absorbance")
        output_text.configure(text="Invalid absorption. Try again.") 



    #  features below are to be implemented
    '''
    use_default = input_validation.get_y_or_n("Use default baselines?")
    if use_default == "n":
        print("Program terminated.\n Edit baselines here: " + path)
        quit()
    '''

    '''
    info_correct = input_validation.get_y_or_n("Is the above information correct?")
    if info_correct == "n":
        protein_used = input_validation.get_float("Enter the amount of protein used (in µL).\n")    
        dilution = input_validation.get_float("Enter the dilution.\n")
    else:
        protein_used = 5
        dilution = 0.1
    dilution_factor = (protein_used/20)*dilution
    # print("dilution factor: " + str(dilution_factor))
    '''

    '''
    a = -0.506713304184884  # values from Excel LINEST function
    b = 1.773611242973140
    c = 0.002712554653342
    '''