import tkinter as tk

assay_calculator = tk.Tk()
assay_calculator.title('Assay Calculator, Rishi Hazra')
width= assay_calculator.winfo_screenwidth()               
height= assay_calculator.winfo_screenheight()               
assay_calculator.geometry("{0}x{1}+0+0".format(assay_calculator.winfo_screenwidth(), assay_calculator.winfo_screenheight()))


label = tk.Label(assay_calculator, text="Michaelis-Menten", font=("Helevicta", 30))
label.grid(row=0, column=10, pady=15)

extinction_input = tk.Entry(assay_calculator, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
extinction_label = tk.Label(assay_calculator, text="Molar Extinction Coefficient (of substrate): ", font=("Helevicta", 17))
extinction_label.grid(row=5, column=10)
extinction_input.grid(row=5, column=11)
concentration_input = tk.Entry(assay_calculator, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
concentration_label = tk.Label(assay_calculator, text="Enzyme Concentration (in µM): ", font=("Helevicta", 17))
concentration_label.grid(row=10, column=10)
concentration_input.grid(row=10, column=11)
data_tracker_status = tk.Label(assay_calculator, text="Off", font=("Helevicta", 12))
data_tracker_value=tk.IntVar()

assay_calculator.mainloop()