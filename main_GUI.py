import tkinter as tk
import tkinter.font
import bradford_assay


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
                            fg='blue', bg='light grey', height=3, width=20, compound="c", 
                            font=("Helevicta", 30))  # mm = michaelis-menten
        mm_btn.place(x=400, y=450)
        ba_btn = tk.Button(self, text="Bradford Assay",
                            command=lambda: controller.show_frame("BradfordAssay"), 
                            fg='purple', bg='light grey', height=3, width=20, compound="c", 
                            font=("Helevicta", 30))  # ba = bradford assay
        ba_btn.place(x=400, y=100)
        mm_btn.pack(pady=20)
        ba_btn.pack(pady=15)


class MichaelisMenten(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Michaelis-Menten", font=controller.title_font)
        label.pack(side="top", fill="x", pady=65)
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
        home_button.place(height=75, width=75)
        extinction_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        extinction_label = tk.Label(self, text="Molar Extinction Coefficient (of substrate): ", font=("Helevicta", 17))
        extinction_label.pack()
        extinction_input.pack(pady=5)
        concentration_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        concentration_label = tk.Label(self, text="Enzyme Concentration (in µM): ", font=("Helevicta", 17))
        concentration_label.pack()
        concentration_input.pack(pady=5)
        data_tracker_status = tk.Label(self, text="Off", font=("Helevicta", 12))
        data_tracker_value=tk.IntVar()
        data_tracker_box = tk.Checkbutton(self, text='In-built Data Tracker', font=("Helevicta", 14), variable=data_tracker_value, onvalue=1, 
                                            offvalue=0, command=lambda: MichaelisMenten.switch_display(self, 
                                            data_tracker_value.get(), data_tracker_status))
        data_tracker_box.pack()
        data_tracker_status.pack()
        output_text = tk.Label(self, text="", font=("Helevicta", 14))
        run_mm_plotter = tk.Button(self, text="Start Michaelis-Menten Assay Calculator", bg='light green', font=("Helevicta", 15),
                                     command=lambda: MichaelisMenten.internal_michaelis_menten(self, extinction_input.get(), 
                                     concentration_input.get(), data_tracker_value.get(), output_text))
        run_mm_plotter.pack(pady=10)
        output_text.pack()  

    def switch_display(master, value, label):
        if value == 1:
            label.configure(text="On")
        elif value == 0:
            label.configure(text="Off")

    def internal_michaelis_menten(master, extinction, concentration, use_data_tracker, output_text):
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
        protein_amount_label = tk.Label(self, text="Protein Amount (µL): ", font=("Helevicta", 17))
        protein_amount_label.pack()
        protein_amount_input.insert(0, "5")
        protein_amount_input.pack(pady=5)
        dilution_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        dilution_label = tk.Label(self, text="Dilution: ", font=("Helevicta", 17))
        dilution_label.pack()
        dilution_input.insert(0, ".1")
        dilution_input.pack(pady=5)
        absorption_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17))
        absorption_label = tk.Label(self, text="Absorption: ", font=("Helevicta", 17))
        absorption_label.pack()
        absorption_input.pack(pady=5)
        output_text = tk.Label(self, text="", font=("Helevicta", 14))
        run_ba = tk.Button(self, text="Get Protein Concentration", bg='light green', font=("Helevicta", 15), command=lambda: bradford_assay.bradford_assay_main(self, protein_amount_input.get(), dilution_input.get(), absorption_input.get(), output_text))
        run_ba.pack(pady=10)  
        output_text.pack()   


    
 
        

    

if __name__ == "__main__":
    root = SampleApp()
    root.title('Assay Calculator, Rishi Hazra')
    width= root.winfo_screenwidth()               
    height= root.winfo_screenheight()               
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()