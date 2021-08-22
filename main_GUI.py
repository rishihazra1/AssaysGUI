import tkinter as tk
import tkinter.font
import michaelis_menten_plotter
import simple_statistics
import math
import bradford_baseline as baseline

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkinter.font.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Home, MichaelisMenten, BradfordAssay):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select desired assay.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        mm_btn = tk.Button(self, text="Michaelis-Menten", 
                            command=lambda: controller.show_frame("MichaelisMenten"), 
                            fg='blue', bg='light grey', height=3, width=20, compound="c", font=("Helevicta", 30))  # mm = michaelis-menten
        mm_btn.place(x=400, y=450)
        ba_btn = tk.Button(self, text="Bradford Assay",
                            command=lambda: controller.show_frame("BradfordAssay"), 
                            fg='purple', bg='light grey', height=3, width=20, compound="c", font=("Helevicta", 30))  # ba = bradford assay
        ba_btn.place(x=400, y=100)
        mm_btn.pack(pady=20)
        ba_btn.pack(pady=15)


class MichaelisMenten(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Michaelis-Menten", font=controller.title_font)
        label.pack(side="top", fill="x", pady=25)
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
        home_button.place(height=75, width=75)
        run_mm_plotter = tk.Button(self, text="Start Michaelis-Menten Assay Calculator", command=lambda: michaelis_menten_plotter.michaelis_menten)
        run_mm_plotter.pack()

class BradfordAssay(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bradford Assay", font=controller.title_font)
        label.pack(side="top", fill="x", pady=65)
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
        home_button.place(height=75, width=75)
        protein_amount_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        protein_amount_label = tk.Label(self, text="Enter Protein Amount (µL): ", font=("Helevicta", 17))
        protein_amount_label.pack()
        protein_amount_input.insert(0, "5")
        protein_amount_input.pack(pady=5)
        dilution_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        dilution_label = tk.Label(self, text="Dilution: ", font=("Helevicta", 17))
        dilution_label.pack()
        dilution_input.insert(0, ".1")
        dilution_input.pack(pady=5)
        absorption_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17))
        absorption_label = tk.Label(self, text="Enter Absorption: ", font=("Helevicta", 17))
        absorption_label.pack()
        absorption_input.pack(pady=5)
        output_text = tk.Label(self, text="", font=("Helevicta", 14))
        run_ba = tk.Button(self, text="Get Protein Concentration", bg='light green', font=("Helevicta", 15), command=lambda: BradfordAssay.internal_bradford_assay(self, protein_amount_input.get(), dilution_input.get(), absorption_input.get(), output_text))
        run_ba.pack(pady=10)  
        output_text.pack()      
        

        
    def internal_bradford_assay(master, protein_used, dilution, absorption, output_text):
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
            output_text.configure(text=str(absorption) + "A →  " + str(concentration) + " mg/mL")     
        except ValueError:
            print("ERROR -- absorbance")
            output_text.configure(text="Invalid absorption. Try again.")     
        

    

if __name__ == "__main__":
    root = SampleApp()
    root.title('Assay Calculator, Rishi Hazra')
    width= root.winfo_screenwidth()               
    height= root.winfo_screenheight()               
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()