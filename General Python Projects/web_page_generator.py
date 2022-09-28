import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # Sets title of window
        self.master.title("Web Page Generator")

        # Creates and positions label informing the user of available actions
        self.lbl = Label(text="Here you can either generate a default HTML page or submit custom text of your own.")
        self.lbl.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        # Creates and positions button to generate default HTML page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        # Creates and positions button to generate HTML page with custom text from entry field
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

        # Creates and places an entry box where user can type a custom message
        self.customEntry = Entry(width=75)
        self.customEntry.grid(row=1, column=0, columnspan=4, padx=(10, 10), pady=(10, 10))

    # This creates a basic web page in a new browser window with default text
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # This creates a basic web page in a new browser window, but with
    # the user's custom text from the entry
    def customHTML(self):
        htmlText = self.customEntry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
