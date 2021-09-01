from tkinter import *
import tkinter.font
import grid_based_michaelis_menten
import grid_based_home
import other_tkinter_functions

assay_calculator = Tk()
assay_calculator.title('Assay Calculator, Rishi Hazra')
width= assay_calculator.winfo_screenwidth()               
height= assay_calculator.winfo_screenheight()               
assay_calculator.geometry("{0}x{1}+0+0".format(assay_calculator.winfo_screenwidth(), assay_calculator.winfo_screenheight()))

label = Label(assay_calculator, text="Select desired assay.", font=("Helevicta, 25"))
label.pack()

home_frame = Frame(assay_calculator)
grid_based_home.build(assay_calculator, home_frame)
michaelis_menten_frame = Frame(assay_calculator)
grid_based_michaelis_menten.build(assay_calculator, michaelis_menten_frame)
michaelis_menten_frame.tkraise()
    
bradford_assay_frame = Frame(assay_calculator)




assay_calculator.mainloop()