import tkinter 

def show_frame(master, page_name):
        '''Show a frame for the given page name'''
        frame = master.frames[page_name]
        frame.tkraise()