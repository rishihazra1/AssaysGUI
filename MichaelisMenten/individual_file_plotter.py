from MichaelisMenten import data_analysis, file_interpreter

def plot_file():
    print("Select the file you wish to plot.")
    path = file_interpreter.request_file()
    data_analysis.plot_single_file(path)
