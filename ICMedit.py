import tkinter as tk
import numpy as np

def get_monitor_height():
    root = tk.Tk()
    height = root.winfo_screenheight()
    #l = np.array([width],[height])
    return ((height))
    
def get_monitor_width():
    root = tk.Tk()
    width = root.winfo_screenwidth()
    #l = np.array([width],[height])
    return ((width))
