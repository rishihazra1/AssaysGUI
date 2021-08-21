import tkinter as tk
import tkinter.font
from BradfordAssay import bradford_assay
from MichaelisMenten import michaelis_menten_plotter
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkinter.font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
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
                            fg='blue', height=10, width=50, compound="c")  # mm = michaelis-menten
        mm_btn.place(x=400, y=450)
        ba_btn = tk.Button(self, text="Bradford Assay",
                            command=lambda: controller.show_frame("BradfordAssay"), 
                            fg='purple', height=10, width=50, compound="c")  # ba = bradford assay
        ba_btn.place(x=400, y=150)
        mm_btn.pack()
        ba_btn.pack()


class MichaelisMenten(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Michaelis-Menten", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        home_button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"))
        home_button.pack()
        run_mm_plotter = tk.Button(self, text="Start Michaelis-Menten Assay Calculator", command=michaelis_menten_plotter.michaelis_menten)
        run_mm_plotter.pack()

class BradfordAssay(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bradford Assay", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("Home"))
        button.pack()
        run_ba = tk.Button(self, text="Bradford Assay: Find Protein Concentration", command=bradford_assay.bradford_assay)
        run_ba.pack()

if __name__ == "__main__":
    root = SampleApp()
    root.title('Assay Calculator, Rishi Hazra')
    width= root.winfo_screenwidth()               
    height= root.winfo_screenheight()               
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()