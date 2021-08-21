import data_analysis
import file_interpreter

print("Select the file you wish to plot.")
path = file_interpreter.request_file()
data_analysis.plot_single_file(path)
