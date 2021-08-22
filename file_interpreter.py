import csv
from tkinter import filedialog 

def request_file():
    path =  filedialog.askopenfilenames(title="Select file.", filetypes=(("CSV Files", "*.csv*"), ("All Files", "*.*")))
    print(path)
    return path


def read_file(csv_file):
    rows = []
    first_column = []
    second_column = []
    with open(csv_file) as current_file:
        csv_reader = csv.reader(current_file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
        index = 0
        while index < len(rows):
            if len(rows[index]) == 0:
                first_column.append("NULL")
                second_column.append("NULL")
            if len(rows[index]) == 1:
                first_column.append(rows[index][0])
                second_column.append("NULL")
            if len(rows[index]) >= 2:
                first_column.append(rows[index][0])
                second_column.append(rows[index][1])
            index += 1
    return first_column, second_column


def initialize_array(time_column, absorption_column):
    x_values = []
    y_values = []
    for index in range(0, len(time_column)):
        if time_column[index] == "HH:MM:SS":
            zero_index = index + 1  # identifying desired data start location
        if time_column[index] == "ID#":
            end_index = index - 2
            break
    t = 0
    for time in range(zero_index, end_index + 1):
        y_values.append(float(absorption_column[time]))
        x_values.append(t)
        t += 1
    print("x_values: " + str(x_values))
    print("y_values: " + str(y_values))
    return x_values, y_values


def get_absorption(y_value_array, time_stamp):
    while True:
        try:
            instantaneous_absorption = y_value_array[time_stamp]
            break
        except IndexError:
            print("Index Error. Data point(s) are missing in given file. Final time will be truncated by 1 second. ")
            time_stamp -= 1
    return instantaneous_absorption


def find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration, molar_extinction):
    slope = (float(end_value) - float(start_value)) / (int(end_time) - int(start_time))
    velocity = (slope * 60) / (float(enzyme_concentration) * float(molar_extinction))
    return velocity
