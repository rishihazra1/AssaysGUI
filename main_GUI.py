import tkinter
from BradfordAssay import bradford_assay
from MichaelisMenten import michaelis_menten_plotter, individual_file_plotter

window = tkinter.Tk()

window.title('Assay Calculator, Rishi Hazra')
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

mm_btn = tkinter.Button(window, text="Michaelis-Menten", fg='blue', height=10, width=50, compound="c")  # mm = michaelis-menten
mm_btn.place(x=400, y=450)
mm_btn.size
ba_btn = tkinter.Button(window, text="Bradford Assay", fg='purple', height=10, width=50, compound="c")  # ba = bradford assay
ba_btn.place(x=400, y=150)

window.mainloop()