
import tkinter
from tkinter import *




class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()
        self.varFName.set('Bob')
        self.varLName.set('Smith')


        print(self.varFName.get())
        print(self.varLName.get())


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
