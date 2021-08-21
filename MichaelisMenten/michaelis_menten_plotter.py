import data_analysis

while True:
    try:
        molar_extinction = float(input("Enter molar extinction coefficient of your substrate.\n"))
        break
    except ValueError:
        print("Input not recognized. Enter the float value.")
while True:
    try:
        enzyme_concentration = float(input("Enter concentration of your enzyme (in µM).\n"))
        break
    except ValueError:
        print("Input not recognized. Enter the float value.")
while True:
    use_data_tracker = input("Would you like to use the in-built data tracker? (yes/no)\n")
    if use_data_tracker == "yes" or use_data_tracker == "no":
        break
    else:
        print("Input not recognized. Enter yes or no.")
trial_concentrations = []
number_of_trials = []
if use_data_tracker == "no":
    concentrations_run = int(input("How many concentrations did you run trials for?\n"))
    print("Enter the concentrations (in µM) at which you ran trials. Press enter after each value.")
    for t in range(0, concentrations_run):
        trial_concentrations.append(input())
    print(trial_concentrations)
    for n in range(0, len(trial_concentrations)):
        number_of_trials.append(int(input("How many trials did you run at  " + trial_concentrations[n] + " µM\n")))
else:
    trial_concentrations, number_of_trials, trial_validity = data_analysis.track_data()
yes_or_no_individual, yes_or_no_overall = data_analysis.time_bound_input_checker()
need_time_bounds = True
if yes_or_no_overall == "yes":
    start_time = int(input("Enter your desired default start_time.\n"))
    end_time = int(input("Enter your desired default end time.\n"))
    need_time_bounds = False
elif yes_or_no_individual == "yes":
    need_time_bounds = False
average_velocities = []
for i in range(0, len(trial_concentrations)):
    temp_value_holder = []  # stores individual trial values per concentration; resets each iteration
    m = 1
    while m < number_of_trials[i] + 1:
        print("Select file with data for Trial " + str(m) + " at " + str(trial_concentrations[i]) + " µM.\n")
        path = data_analysis.file_interpreter.request_file()
        first_column, second_column = data_analysis.file_interpreter.read_file(path)
        x_values, y_values = data_analysis.file_interpreter.initialize_array(first_column, second_column)
        if yes_or_no_individual == "yes":
            start_time, end_time = data_analysis.get_time_bounds(x_values)
            need_time_bounds = False
        if need_time_bounds is True:
            start_time, end_time = data_analysis.find_best_bounds(x_values, y_values)
            print("bounds: " + str(start_time) + ", " + str(end_time))
        start_value = data_analysis.file_interpreter.get_absorption(y_values, start_time)
        end_value = data_analysis.file_interpreter.get_absorption(y_values, end_time)
        velocity = abs(
            data_analysis.file_interpreter.find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration,
                                           molar_extinction))
        temp_value_holder.append(velocity)
        print("velocities: " + str(temp_value_holder))
        m += 1
    index = 0
    velocity_sum = 0
    for index in range(0, m - 1):
        velocity_sum += temp_value_holder[index]
    concentration_velocity_average = velocity_sum / (m - 1)
    average_velocities.append(concentration_velocity_average)
print("Average Velocities: " + str(average_velocities))
print("Generating Michaelis-Menten plot, please wait.")
data_analysis.plot_from_arrays(trial_concentrations, average_velocities)