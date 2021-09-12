import tkinter as tk
import tkinter.font
import bradford_assay
import bradford_baseline as bb
import functools

class SampleApp(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__( self, parent)
        
        self.parent=parent
        #self.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.title('Assay Calculator, Rishi Hazra')
        self.title_font = tkinter.font.Font(family='Helvetica', size=30, weight="bold", slant="italic")          
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(True, True)
        self.columnconfigure(0, weight=1)
                
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

    def onClosing(self):
        if (tk.messagebox.askokcancel("Change Default Baseline", "Override default baseline with last saved?")):
            bb.override_default_baseline()
            if tk.messagebox.showinfo(title='Default baseline override', message = 'Default baseline overridden with last saved baseline'):
                self.destroy()
        else:
            self.destroy()            
        

class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        parent.columnconfigure(0,weight=1)
        parent.columnconfigure(1,weight=1)
        parent.columnconfigure(2,weight=1)  
        
        label = tk.Label(self, text="Select desired assay", font=controller.title_font)
        label.grid(column=1,row=0,sticky=tk.W, padx=420, pady=30)

        mm_btn = tk.Button(self, text="Michaelis-Menten", 
                            command=lambda: controller.show_frame("MichaelisMenten"), 
                            fg='blue', bg='maroon', width=20, compound="c", 
                            font=("Helevicta", 30))  # mm = michaelis-menten
   #     mm_btn.grid(column=1,row=1,sticky=tk.W)

        ba_btn = tk.Button(self, text="Bradford Assay",
                            command=lambda: controller.show_frame("BradfordAssay"), 
                            fg='white', bg='maroon', width=20, compound="c", 
                            font=("Helevicta", 30))  # ba = bradford assay
        ba_btn.grid(column=1,row=1)

   
class BradfordAssay(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        parent.columnconfigure(0,weight=1)
        parent.columnconfigure(1,weight=1)
        parent.columnconfigure(2,weight=1)
        parent.columnconfigure(3,weight=1)  
         

        label = tk.Label(self, text="Bradford Assay", font=controller.title_font)
        label.grid(column=1,row=1, padx=40, pady=10, columnspan=30, sticky=tk.W)
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
        home_button.grid(column=0, row=0)

        baseline_btn = tk.Button(self, text="Modify Baselines",
                            command=lambda: controller.show_frame("BradfordAssayBaseline"), 
                            bg='yellow', fg="black", font=("Helevicta", 15))  # ba = bradford assay baseline
        baseline_btn.grid(column=2, row=5, pady=15, sticky=tk.W)

        protein_amount_label = tk.Label(self, text="Protein Amount (µL): ", font=("Helevicta", 17))
        protein_amount_label.grid(column=1,row=2, pady=8, sticky=tk.E)
        protein_amount_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        protein_amount_input.grid(column=2,row=2, padx=15, sticky=tk.W)
        protein_amount_input.insert(0, "5")        

        dilution_label = tk.Label(self, text="Dilution: ", font=("Helevicta", 17))
        dilution_label.grid(column=1,row=3, pady=8, sticky=tk.E)
        dilution_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17)) 
        dilution_input.grid(column=2,row=3, padx=15, sticky=tk.W)
        dilution_input.insert(0, ".1")
        
        absorption_label = tk.Label(self, text="Absorption: ", font=("Helevicta", 17))
        absorption_label.grid(column=1,row=4, pady=8, sticky=tk.E)
        absorption_input = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17))
        absorption_input.grid(column=2,row=4, padx=15, sticky=tk.W)

        defaultSelected=tk.IntVar()
        doPlot=tk.IntVar()

        frame = tk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(0, weight=3)
        tk.Checkbutton(frame, text="Include Default baseline", variable=defaultSelected, font=("Helevicta", 11)).grid(column=0, row=0)
        tk.Checkbutton(frame, text="Plot", variable=doPlot, font=("Helevicta", 11)).grid(column=1, row=0)
        frame.grid(column=3,row=7)
        
        stored_baseline_result_text = tk.Label(self, text="", font=("Helevicta", 20))
        stored_baseline_result_text.grid(column=2,row=8, pady=15)
        default_baseline_result_text = tk.Label(self, text="", font=("Helevicta", 20))
        default_baseline_result_text.grid(column=2,row=9, pady=15)

        run_ba = tk.Button(self, text="Calculate Protein Concentration", bg='light green', font=("Helevicta", 15), command=lambda: bradford_assay.bradford_assay_main(self, protein_amount_input.get(), dilution_input.get(), absorption_input.get(), stored_baseline_result_text, default_baseline_result_text, defaultSelected.get(),doPlot.get()))
        run_ba.grid(column=2,row=7, sticky=tk.W)

        self.entries = []

class BradfordAssayBaseline(tk.Frame):
    
    global fileSaved
    global entryChanged
    entryChanged=False       
    fileSaved=False   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bb.create_master_baseline()
    
        parent.columnconfigure(0,weight=1)
        parent.columnconfigure(1,weight=1)
        parent.columnconfigure(2,weight=1)
        parent.columnconfigure(3,weight=1)
        parent.columnconfigure(4,weight=1)
        
        rowCount=0
        
        '''
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"), bg="sky blue", fg="black", font=("Helevicta", 15))
        home_button.grid(column=0,row=rowCount)

        '''   
        message_text = tk.Label(self, text="", font=("Helevicta", 20))
        bradfordAssay_button = tk.Button(self, text="Back", bg="sky blue", fg="black", font=("Helevicta", 15),
                           command=lambda: handle_unsaved_changes(self, controller, message_text))
        bradfordAssay_button.grid(column=0,row=rowCount)

        rowCount+=1
        label = tk.Label(self, text="Bradford Assay Baselines", font=controller.title_font)
        label.grid(column=1, row=rowCount, padx=200, pady=10, columnspan=6)

        fields = bb.get_baseline_fields()
        rowCount+=1
        columnCount = 0
        for i in range(0, len(fields)):
            label = tk.Label(self, text=fields[i], font=("Helevicta", 17))
            label.grid(column=i,row=rowCount, padx=15)
            columnCount+=1

        default_values = bb.read_stored_baseline_without_header(bb.last_saved_file_name)
        for i in range(0, len(default_values)):
            currentRow = default_values[i]
            rowCount+=1
            columnCount=0
            for j in range(0, len(currentRow)):
                globals()[f"input_{i}_{j}"] = tk.Entry(self, bg="light grey", fg="black", bd="3", font=("Helevicta", 17), width=6)
                globals()[f"input_{i}_{j}"].grid(column=columnCount,row=rowCount)
                globals()[f"input_{i}_{j}"].insert(0, currentRow[j])
                globals()[f"input_{i}_{j}"].bind('<Key>', functools.partial(trackChanges, param=message_text))
                columnCount+=1
        
        #Add button to update
        rowCount+=1
        
        message_text.grid(column=1, columnspan=4, row=rowCount, pady=15)

        store_ba = tk.Button(self, text="Save ", bg='light green', font=("Helevicta", 20), command=lambda: handle_modified_baseline(message_text))
        store_ba.grid(column=0,row=rowCount, pady=15)
        read_saved_ba = tk.Button(self, text="Show Last Saved", bg='light green', font=("Helevicta", 15), command=lambda: setEntryValues(self,bb.read_stored_baseline(bb.last_saved_file_name, message_text)))
        read_saved_ba.grid(column=5,row=3, padx=30)
        get_default_ba = tk.Button(self, text="Show Default", bg='light green', font=("Helevicta", 15), command=lambda: setEntryValues(self,bb.read_stored_baseline(bb.default_baseline_file_name, message_text)))
        get_default_ba.grid(column=5,row=4, padx=30, pady=8)
        restore_ba = tk.Button(self, text="Restore Default with master", bg='dark red', fg="white", font=("Helevicta", 15), command=lambda: bb.restore_default_baseline(message_text))
        restore_ba.grid(column=5, pady=50, row=rowCount+1)

def trackChanges(event, param):
    global entryChanged
    entryChanged=True
    param.configure(text="") 


def handle_unsaved_changes(self, controller, message_text):
    global entryChanged
    global fileSaved

    if(entryChanged):
        if (tk.messagebox.askokcancel("Save changes", "Some values are changed in the grid. Do you want to save the baseline?")):
            handle_modified_baseline(message_text) 
        else:
            setEntryValues(self,bb.read_stored_baseline(bb.last_saved_file_name, message_text))
        entryChanged = False  
         
    if(fileSaved):
        if (tk.messagebox.askokcancel("Default Baseline", "File saved. Override default baseline with last saved?")):
            bb.override_default_baseline()
            tk.messagebox.showinfo(title='Default baseline override', message = 'Default baseline overridden with last saved baseline') 
        
        fileSaved = False

    controller.show_frame("BradfordAssay")

def handle_modified_baseline(message_text):
    global fileSaved
    global entryChanged

    bb.save_modified_baseline(getEntryValuesWithHeader(),message_text)
    
    fileSaved=True
    entryChanged=False

def setEntryValues(frame,table):
    row = []
    rowNumber=0
    for row in table:
        columnNumber=0
        if (rowNumber!=0):
            for column in row:
                globals()[f"input_{rowNumber-1}_{columnNumber}"].delete(0, 100)
                globals()[f"input_{rowNumber-1}_{columnNumber}"].insert(0, column)
                columnNumber+=1
        rowNumber+=1
    return

def getEntryValuesWithoutHeader():
    table = []
    
    fields = bb.get_baseline_fields() 
    for i in range(0, 6):
        row = []    
        for j in range(0, len(fields)):
            row.append(globals()[f"input_{i}_{j}"].get()) 
        table.append(row)
    return table

def getEntryValuesWithHeader():
    table = []
    
    row = []
    fields = bb.get_baseline_fields()  
    for i in range(0, len(fields)):
        row.append(fields[i])
    table.append(row)
    
    default_values = bb.get_default_baseline_values()
    for i in range(0, 6):
        row = []    
        for j in range(0, len(fields)):
            row.append(globals()[f"input_{i}_{j}"].get()) 
        table.append(row)
    return table

if __name__ == "__main__":
    root=SampleApp(None)
    root.mainloop()
    
    