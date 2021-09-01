import tkinter as tk

def build(master, frame):
    label = tk.Label(frame, text="Select desired assay.", font=("Helevicta, 25"))
    label.pack(side="top", fill="x", pady=10)

    mm_btn = tk.Button(frame, text="Michaelis-Menten", 
                        command=lambda: master.show_frame("MichaelisMenten"), 
                        fg='blue', bg='light grey', height=3, width=20, compound="c", 
                        font=("Helevicta", 30))  # mm = michaelis-menten
    mm_btn.place(x=400, y=450)
    ba_btn = tk.Button(frame, text="Bradford Assay",
                        command=lambda: master.show_frame("BradfordAssay"), 
                        fg='purple', bg='light grey', height=3, width=20, compound="c", 
                        font=("Helevicta", 30))  # ba = bradford assay
    ba_btn.place(x=400, y=100)
    mm_btn.pack(pady=20)
    ba_btn.pack(pady=15)