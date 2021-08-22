import bradford_baseline as baseline
import simple_statistics
import math

def bradford_assay_main(master, protein_used, dilution, absorption, output_text):
    try:
            protein_used = float(protein_used)
    except ValueError:
        print("ERROR -- protein_amount")
        output_text.configure(text="Invalid protein amount entered. Try again.")
    try:
        dilution = float(dilution)
    except ValueError:
        print("ERROR -- dilution")
        output_text.configure(text="Invalid dilution entered. Try again.")        
    baselines = [['20', '0', '1.000', '1.258', '1.155'], ['15', '5', '0.750', '1.083', '1.098'], ['10', '10', '0.500', '0.728', '0.713'], ['5', '15', '0.250', '0.422', '0.402'], ['2.5', '17.5', '0.125', '0.223', '0.214'], ['0', '20', '0.000', '0', '-0.005']]
    print("protein_used: " + str(protein_used))
    print("dilution: " + str(dilution))
    x_terms, y_terms = baseline.calculate_baselines(baselines)
    dilution_factor = (protein_used/20)*dilution
    a, b, c = simple_statistics.get_best_fit_line(x_terms, y_terms)  # values generated through numpy polyfit
    r_squared = simple_statistics.get_r_squared(x_terms, y_terms, a, b, c)
    print("a = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c))
    try:   
        concentration = ((-b + math.sqrt(b**2 - 4*a*c + 4*a*float(absorption)))/(2*a))/dilution_factor
        print("protein concentration (mg/mL): " + str(concentration))
        output_text.configure(text=str(absorption) + "A →  " + str(concentration) + " mg/mL\n" + "r² = " + str(r_squared))     
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

    
