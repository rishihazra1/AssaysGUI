import matplotlib.pyplot as plt
import numpy as np
from MichaelisMenten import file_interpreter
import scipy 
import os
# functions below originally from other_functions.py

def get_time_bounds(data_set):
    while True:
        yes_or_no = input("Would you like to select a specific range to plot? Enter yes or no.\n")
        if str.lower(yes_or_no) == "no":
            start = 0
            end = len(data_set) - 1
            break
        elif str.lower(yes_or_no) == "yes":
            start = int(input("Enter your desired start time for the plot.\n"))
            end = int(input("Enter your desired end time for the plot.\n"))
            break
        else:
            print("Input not recognized. Enter yes or no.")
    return start, end


def time_bound_input_checker():
    yes_or_no_overall = "no"
    while True:
        yes_or_no_individual = input("Do you have different desirable time bounds for each file?\n")
        if str.lower(yes_or_no_individual) == "yes" or str.lower(yes_or_no_individual) == "no":
            break
        else:
            print("Input not recognized. Please enter yes or no.")
    if yes_or_no_individual == "no":
        while True:
            yes_or_no_overall = input("Do you have a default desirable time bound for all files?\n")
            if str.lower(yes_or_no_overall) == "yes" or str.lower(yes_or_no_overall) == "no":
                break
            else:
                print("Input not recognized. Please enter yes or no.")
    return yes_or_no_individual, yes_or_no_overall


def convert_to_numpy_float(x_array, y_array):
    x_numpy = np.array(x_array).astype(np.float64)
    y_numpy = np.array(y_array).astype(np.float64)
    return x_numpy, y_numpy


def convert_to_numpy_array(x_array, y_array):
    x_numpy = np.array(x_array)
    y_numpy = np.array(y_array)
    return x_numpy, y_numpy


def get_predicted_y(x_numpy, slope, intercept):
    print(x_numpy)
    predicted_y = []
    for i in range(0, len(x_numpy)):
        predicted_y.append((x_numpy[i] * slope) + intercept)
    return predicted_y




#  functions below from original graph_functions.py

def plot_single_file(file):
    first_column, second_column = file_interpreter.read_file(file)
    all_x_values, all_y_values = file_interpreter.initialize_array(first_column, second_column)
    desired_x_values = []
    desired_y_values = []
    start, end = get_time_bounds(all_y_values)
    index = start
    while index <= end:
        try:
            desired_y_values.append(float(all_y_values[index]))
            index += 1
        except IndexError:
            print(
                "Index Error. Data point(s) are missing in given file. Plot will be truncated to the length of your "
                "data set. ")
            break
    print("y-values: " + str(desired_y_values))
    for time in range(start, index):
        desired_x_values.append(time)
    print("x-values: " + str(desired_x_values))
    x_numpy, y_numpy = convert_to_numpy_float(desired_x_values, desired_y_values)
    plt.scatter(x_numpy, y_numpy, s=10)
    plt.plot()
    plot_best_fit_line(x_numpy, y_numpy)


def plot_from_arrays(x_array, y_array):  # note that errors can occur due to incorrect data files (data from certain seconds missing from file).
    print(x_array, y_array)
    x_numpy, y_numpy = convert_to_numpy_float(x_array, y_array)
    plt.scatter(x_numpy, y_numpy, s=10)
    plot_best_fit_line(x_numpy, y_numpy)


def plot_best_fit_line(x_numpy, y_numpy):
    result = scipy.stats.linregress(x_numpy, y_numpy)
    r_squared = float(result.rvalue) ** 2
    print(f"r_squared: {r_squared}")
    print(str(result.slope) + ", " + str(result.intercept))
    plt.plot(x_numpy, result.intercept + result.slope * x_numpy)
    plt.show()
    print("Plot opened in alternate window.")
    return result, r_squared


def get_r_squared(x_numpy, y_numpy):
    result = scipy.stats.linregress(x_numpy, y_numpy)
    r_squared = float(result.rvalue) ** 2
    return r_squared


def find_best_bounds(x_values, y_values):
    max_r_squared = 0
    max_bounds = [0, len(x_values) - 1, "ERROR: reverted to full plot"]
    for start_index in range(0, len(x_values) - 15):
        for end_index in range(start_index + 15, len(x_values)):
            new_x_values = []
            new_y_values = []
            i = start_index
            while i < end_index + 1:
                new_x_values.append(x_values[i])
                new_y_values.append(y_values[i])
                i += 1
            print("new_x_values: " + str(new_x_values))
            print("new_y_values: " + str(new_y_values))
            new_x_numpy, new_y_numpy = convert_to_numpy_float(new_x_values, new_y_values)
            r_squared = get_r_squared(new_x_numpy, new_y_numpy)
            print(start_index, end_index, r_squared)
            if r_squared == 1 or r_squared == 0:
                print("Calculated r-value incorrect.")
            elif max_r_squared < r_squared:
                max_bounds = [start_index, end_index, r_squared]
                max_r_squared = r_squared
                print("New max at: " + str(max_bounds))
    print(max_bounds)
    return max_bounds[0], max_bounds[1]


# files below from original data_tracker.py 

def track_data():
    concentrations = []
    trials_per_concentration = []
    data = []
    trial_validity = []
    all_data = []
    index_tracker = 0
    while True:  # terminates when there are no more concentrations
        while True:  # terminates with valid user input
            next_occurrence = input("Enter the current substrate concentration (in µM). Enter 'no' to exit "
                                    "loop.\n")
            if next_occurrence == "no":
                break
            try:
                concentrations.append(float(next_occurrence))
                break
            except ValueError:
                print("Input not recognized. Enter the concentration or enter 'no' to exit loop.")
        if next_occurrence == "no":
            break
        current_trial = 0
        while True:  # terminates when there are no more trials for current concentration
            current_trial += 1
            while True:
                next_trial_input = input("Enter data for Trial " + str(current_trial) + " at " + str(
                    next_occurrence) + " µM. Enter 'no' to exit loop.\n")
                if next_trial_input == "no":
                    current_trial -= 1
                    break
                try:
                    data.append(float(next_trial_input))
                    break
                except ValueError:
                    print("Input not recognized. Enter the data value or enter 'no' to exit loop.")
            if next_trial_input == "no":
                break
            while True:  # terminates when user input for trial_validity is valid
                keep_trial = input("Would you like to keep the data for Trial " + str(current_trial) + " ? (yes/no)\n")
                if keep_trial == "yes":
                    trial_validity.append(True)
                    break
                elif keep_trial == "no":
                    trial_validity.append(False)
                    break
                else:
                    print("Input not recognized. Enter the concentration or enter 'no' to exit loop.")
            print(current_trial)
            temp_array = [next_occurrence, next_trial_input, trial_validity[len(trial_validity) - 1]]
            all_data.insert(index_tracker, temp_array)
            index_tracker += 1
            print(all_data)
        trials_per_concentration.append(int(current_trial))
    print("all_data: " + str(all_data))
    # writing csv
    fields = ['Concentration', 'Rate', 'Trial Validity']
    rows = all_data
    file_name = file_interpreter.filedialog.askdirectory()
    file_saved = False
    i = 1
    while file_saved is False:
        try:
            with open(file_name, 'w') as csvfile:
                csvwriter = file_interpreter.csv.writer(csvfile)
                csvwriter.writerow(fields)
                csvwriter.writerow(rows)
            file_saved = True
            if i == 1:
                file_location = file_name
        except PermissionError:
            print("Insufficient permissions. Storing in local directory instead.\n Enter desired file name.")
            file_name = str(input()) + ".csv"
            file_location = os.path.join(r"C:\Users\hazra\Documents\GitHub\Michaelis-Menten", file_name)
            file_saved = False
        i += 1
    print("Stored at " + str(file_location) + " Ctrl + Click to open.")
    return file_location  