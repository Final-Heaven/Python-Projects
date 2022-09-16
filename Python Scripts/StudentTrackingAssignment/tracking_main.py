# Python Version: 3.10.6
#
# Author:         Daniel Castillo
#
# Purpose:        Student Tracking Assignment. Similar to the phonebook
#                 demo, but with adjusted features.


from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Be sure to import our other modules so we can have access to them
import tracking_gui
import tracking_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500, 400) #(Height, Width)
        self.master.maxsize(500, 400)
        # This CenterWindow method will center our app on the user's screen
        tracking_func.center_window(self, 500, 300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter build-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: tracking_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and cluster free
        tracking_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
