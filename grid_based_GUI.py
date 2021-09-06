import tkinter as tk
import tkinter.font
import bradford_assay
import bradford_baseline as bb


class SampleApp(tk.Tk):
    #testing
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__( self, *args, **kwargs)

        self.title('Assay Calculator, Rishi Hazra')
        self.title_font = tkinter.font.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        width= self.winfo_screenwidth()               
        height= self.winfo_screenheight()               
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(0,0)
        self.columnconfigure(0,weight=1)
                
        container=self  
        self.frames = {}
       
        for F in (Home, BradfordAssay, BradfordAssayBaseline):
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

        parent.columnconfigure(0,weight=1)
        parent.columnconfigure(1,weight=1)
        parent.columnconfigure(2,weight=1)  


        label = tk.Label(self, text="Select desired assay", font=controller.title_font)
        label.grid(column=1,row=0,sticky=tk.W)

        mm_btn = tk.Button(self, text="Michaelis-Menten", 
                            command=lambda: controller.show_frame("MichaelisMenten"), 
                            fg='blue', bg='light grey', width=20, compound="c", 
                            font=("Helevicta", 30))  # mm = michaelis-menten
        mm_btn.grid(column=1,row=1,sticky=tk.W)

        ba_btn = tk.Button(self, text="Bradford Assay",
                            command=lambda: controller.show_frame("BradfordAssay"), 
                            fg='purple', bg='light grey', width=20, compound="c", 
                            font=("Helevicta", 30))  # ba = bradford assay
        ba_btn.grid(column=1,row=1,sticky=tk.W)

   
class BradfordAssay(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        parent.columnconfigure(0,weight=1)
        parent.columnconfigure(1,weight=1)
        parent.columnconfigure(2,weight=1)
        

        label = tk.Label(self, text="Bradford Assay", font=controller.title_font)
        label.grid(column=1,row=0, columnspan=2)
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
        home_button.grid(column=0,row=0)

        protein_amount_label = tk.Label(self, text="Enter Protein Amount (µL): ", font=("Helevicta", 17))
        protein_amount_label.grid(column=1,row=1)
        protein_amount_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        protein_amount_input.grid(column=2,row=1)
        protein_amount_input.insert(0, "5")
        

        dilution_label = tk.Label(self, text="Dilution: ", font=("Helevicta", 17))
        dilution_label.grid(column=1,row=2)
        dilution_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        dilution_input.grid(column=2,row=2)
        dilution_input.insert(0, ".1")
        
        absorption_label = tk.Label(self, text="Enter Absorption: ", font=("Helevicta", 17))
        absorption_label.grid(column=1,row=3)
        absorption_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17))
        absorption_input.grid(column=2,row=3)

        output_text = tk.Label(self, text="", font=("Helevicta", 14))
        output_text.grid(column=3,row=4)
        run_ba = tk.Button(self, text="Get Protein Concentration", bg='light green', font=("Helevicta", 15), command=lambda: bradford_assay.bradford_assay_main(self, protein_amount_input.get(), dilution_input.get(), absorption_input.get(), output_text))
        run_ba.grid(column=2,row=4)

        baseline_btn = tk.Button(self, text="Bradford Assay baseline",
                            command=lambda: controller.show_frame("BradfordAssayBaseline"), 
                            bg='light green', font=("Helevicta", 15))  # ba = bradford assay baseline
        baseline_btn.grid(column=2,row=5)

        self.entries = []

class BradfordAssayBaseline(tk.Frame):
                   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        parent.columnconfigure(0,weight=1)
        parent.columnconfigure(1,weight=1)
        parent.columnconfigure(2,weight=1)
        parent.columnconfigure(3,weight=1)
        parent.columnconfigure(4,weight=1)
        parent.columnconfigure(5,weight=1)       
        parent.columnconfigure(6,weight=1)

        rowCount=0
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
        home_button.grid(column=0,row=rowCount)

        bradfordAssay_button = tk.Button(self, text="BradfordAssay",
                           command=lambda: controller.show_frame("BradfordAssay"), bg="sky blue", fg="black", font=("Helevicta", 15))
        bradfordAssay_button.grid(column=1,row=rowCount)
        
        rowCount+=1
        label = tk.Label(self, text="Bradford Assay Baseline", font=controller.title_font)
        label.grid(column=0,row=rowCount,columnspan=6)

        fields = bb.get_baseline_fields()
        rowCount+=1
        columnCount = 0
        for i in range(0, len(fields)):
            label = tk.Label(self, text=fields[i], font=("Helevicta", 17))
            label.grid(column=i,row=rowCount)
            columnCount+=1

        calculated_fields = bb.get_calculated_baseline_fields()
        for j in range(0,len(calculated_fields)):
            label = tk.Label(self, text=calculated_fields[j], font=("Helevicta", 17))
            label.grid(column=columnCount,row=rowCount)
            columnCount+=1

        default_values = bb.get_default_baseline_values()
        
        for i in range(0, len(default_values)):
            currentRow = default_values[i]
            rowCount+=1
            columnCount=0
            
            for j in range(0, len(currentRow)):
                globals()[f"input_{i}_{j}"] = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17), width=6) 
                globals()[f"input_{i}_{j}"].grid(column=columnCount,row=rowCount)
                globals()[f"input_{i}_{j}"].insert(0, currentRow[j])
                columnCount+=1
            #Total volume    
            volume_label = tk.Label(self, text=(float (currentRow[0]))+ (float (currentRow[1])), font=("Helevicta", 17))
            volume_label.grid(column=columnCount,row=rowCount)
            columnCount+=1
            #A_562 (avg)
            avg_label = tk.Label(self, text=(float(currentRow[3])+ float(currentRow[4]))/2, font=("Helevicta", 17))
            avg_label.grid(column=columnCount,row=rowCount)
        #Add button to update
        rowCount+=1
        store_ba = tk.Button(self, text="Save baseline", bg='light green', font=("Helevicta", 15), command=lambda: bb.save_modified_baseline(getEntryValues()))
        store_ba.grid(column=0,row=rowCount)
        read_saved_ba = tk.Button(self, text="Last Saved", bg='light green', font=("Helevicta", 15), command=lambda: bb.read_stored_baseline())
        read_saved_ba.grid(column=1,row=rowCount)
        get_default_ba = tk.Button(self, text="Default baseline", bg='light green', font=("Helevicta", 15), command=lambda: bb.get_default_baseline())
        get_default_ba.grid(column=2,row=rowCount)


def getEntryValues():
    rows = [[]]
    
    fields = bb.get_baseline_fields()
    print(fields)
    print(fields[0])
    rowCount = 0
    columnCount = 0
    for i in range(0, len(fields)):
        print(i,rowCount,columnCount)
        rows[rowCount][columnCount] = fields[i]
        columnCount+=1

    calculated_fields = bb.get_calculated_baseline_fields()
    for j in range(0,len(calculated_fields)-1):
        rows[rowCount][columnCount]=calculated_fields[j]
        columnCount+=1

    default_values = bb.get_default_baseline_values()
    for i in range(0, 5):
            rowCount+=1
            columnCount=0
            
            for j in range(0, len(fields)):
                rows[rowCount][columnCount] = globals()[f"input_{rowCount}_{columnCount}"].get()
                columnCount+=1
            for j in range(0, len(calculated_fields)):
                rows[rowCount][columnCount] = globals()[f"input_{rowCount}_{columnCount}"].get()
                columnCount+=1
    return rows

if __name__ == "__main__":
    root = SampleApp()
    root.mainloop()