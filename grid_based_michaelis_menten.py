from michaelis_menten_plotter import michaelis_menten
import tkinter as tk
import tkinter.font

def build(master, frame):
    label = tk.Label(frame, text="Michaelis-Menten", font=("Helevicta", 30))
    label.grid(row=0, column=10, pady=15)
    home_button = tk.Button(frame, text="HOME",
                        command=lambda: master.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
    home_button.place(height=75, width=75)
    extinction_input = tk.Entry(frame, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
    extinction_label = tk.Label(frame, text="Molar Extinction Coefficient (of substrate): ", font=("Helevicta", 17))
    extinction_label.grid(row=5, column=10)
    extinction_input.grid(row=5, column=11)
    concentration_input = tk.Entry(frame, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
    concentration_label = tk.Label(frame, text="Enzyme Concentration (in µM): ", font=("Helevicta", 17))
    concentration_label.grid(row=10, column=10)
    concentration_input.grid(row=10, column=11)
    data_tracker_status = tk.Label(frame, text="Off", font=("Helevicta", 12))
    data_tracker_value=tk.IntVar()
    data_tracker_box = tk.Checkbutton(frame, text='In-built Data Tracker', font=("Helevicta", 14), variable=data_tracker_value, onvalue=1, 
                                        offvalue=0, command=lambda: switch_display(frame, 
                                        data_tracker_value.get(), data_tracker_status))
    data_tracker_box.grid(row=15, column=10)
    data_tracker_status.grid(row=15, column=11)
    output_text = tk.Label(frame, text="", font=("Helevicta", 14))
    data_tracker_box.select()
    if data_tracker_value.get() == 0:
        concentrations_input = tk.Entry(frame, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        concentrations_label = tk.Label(frame, text="Enter Total Concentrations Run: ", font=("Helevicta", 17))
        concentrations_label.grid(row=20, column=10)
        concentrations_input.grid(row=20, column=11)
    run_mm_plotter = tk.Button(frame, text="Start Michaelis-Menten Assay Calculator", bg='light green', font=("Helevicta", 15),
                                    command=lambda: internal_michaelis_menten(frame, extinction_input.get(), 
                                    concentration_input.get(), data_tracker_value.get(), output_text))
    run_mm_plotter.grid(row=25, column=10)
    output_text.grid(row=27, column=10)  
    frame.tkraise()

def switch_display(value, label):
        if value == 1:
            label.configure(text="On")
        elif value == 0:
            label.configure(text="Off")

def internal_michaelis_menten(frame, extinction, concentration, use_data_tracker, output_text):
        valid_concentration = False
        valid_extinction = False
        try:
            molar_extinction = float(extinction)
            valid_extinction = True
        except ValueError:
            output_text.configure(text="Invalid extinction coefficient. Try again.")
        try:
            enzyme_concentration = float(concentration)
            valid_concentration = True
        except ValueError:
            output_text.configure(text="Invalid enzyme concentration. Try again.")
        if valid_extinction is True and valid_concentration is True:
            print("THIS LOCATION")
            output_text.configure(text="Loading Enzyme Kinetics Calculator")
            if use_data_tracker == 1:
                print("ALSO HERE")
                output_text.configure(text="Loading In-Built Data Tracker")            
         #   michaelis_menten_plotter.michaelis_menten(master, extinction, concentration, use_data_tracker, output_text)
        if use_data_tracker == 0:
            concentrations_run = int(input("How many concentrations did you run trials for?\n"))
            print("Enter the concentrations (in µM) at which you ran trials. Press enter after each value.")
            
       
    