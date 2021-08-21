import tkinter
from BradfordAssay import bradford_assay
from MichaelisMenten import michaelis_menten_plotter, individual_file_plotter

window = tkinter.Tk()
window.title('Assay Calculator, Rishi Hazra')
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.mainloop()