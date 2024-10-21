"""
Main module for the application.
"""

import tkinter as tk
from Object.draw_interface import DrawInterface

if __name__ == "__main__":
    root = tk.Tk()
    print("Creating the dataset...")
    interface = DrawInterface(root)
    root.mainloop()
