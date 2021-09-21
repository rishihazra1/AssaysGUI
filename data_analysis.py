import matplotlib.pyplot as plt
from numpy import array, float64
import file_interpreter
from scipy.stats import linregress
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
    x_numpy = array(x_array).astype(float64)
    y_numpy = array(y_array).astype(float64)
    return x_numpy, y_numpy


def convert_to_numpy_array(x_array, y_array):
    x_numpy = array(x_array)
    y_numpy = array(y_array)
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
    plt.xlabel('BSA Concentration')
    plt.ylabel('Average Absorption')
    
    x_numpy, y_numpy = convert_to_numpy_float(x_array, y_array)
    plt.scatter(x_numpy, y_numpy, s=6, marker='.')
    plot_best_fit_line(x_numpy, y_numpy, "last saved baseline")

    plt.legend(loc='upper left')
    plt.show()

def plot_from_2_arrays(x_array_1, y_array_1, x_array_2, y_array_2):  # note that errors can occur due to incorrect data files (data from certain seconds missing from file).
    plt.xlabel('BSA Concentration')
    plt.ylabel('Average Absorption')

    x_numpy, y_numpy = convert_to_numpy_float(x_array_1, y_array_1)
    plt.scatter(x_numpy, y_numpy, s=6, marker='^')
    plot_best_fit_line(x_numpy, y_numpy, "dafault baseline")
    
    x_numpy, y_numpy = convert_to_numpy_float(x_array_2, y_array_2)
    plt.scatter(x_numpy, y_numpy, s=6, marker='.')
    plot_best_fit_line(x_numpy, y_numpy, "last saved baseline")
    
    plt.legend(loc='upper left')
    plt.show()

def plot_best_fit_line(x_numpy, y_numpy, myLabel):
    result = linregress(x_numpy, y_numpy)
    r_squared = float(result.rvalue) ** 2
    plt.plot(x_numpy, result.intercept + result.slope * x_numpy, label=myLabel)
    return result, r_squared


def get_r_squared(x_numpy, y_numpy):
    result = linregress(x_numpy, y_numpy)
    r_squared = float(result.rvalue) ** 2
    return r_squared

