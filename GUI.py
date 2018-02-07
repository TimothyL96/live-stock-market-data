import tkinter as tk
from tkinter import *
from tkinter import messagebox
import APItoXML
import XMLtoCSV
import CSVtoExcel
# Written by
# Teoh Jie Sheng
# A GUI for TSW assignemnt

class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.size()
        self.grid()
        # self.grid_rowconfigure(0, minsize=200)
        # self.grid_rowconfigure(1, minsize=200)
        self.createFirstRow()
        self.createSecondRow()
        self.createButtonRow()

    def createFirstRow(self):
        Label(self, text="Symbol of Stock: ").grid(row=0, column=0)
        sharelist = ['MSFT', 'GOOGL', 'AAPL', 'FB']
        var = tk.StringVar(root)
        var.set('Please Select')
        sharedropdown = OptionMenu(root, var, *sharelist, command=self.share_value)
        sharedropdown.grid(row=0, column=1, rowspan=2)

    def createSecondRow(self):
        Label(self, text="Report Type: ").grid(row=1, column=0)
        optionlist = ['DAILY', 'WEEKLY', 'MONTHLY']
        var = tk.StringVar(root)
        var.set('Please Select')
        sharedropdown = OptionMenu(root, var, *optionlist, command=self.option_value)
        sharedropdown.grid(row=1, column=1, rowspan=2)

    def helloCallBack(self):
        if messagebox.askyesno("Confirmation", "Are you sure about your decision?", icon='warning') == True:
            a = [self.share_select, self.option_select]
            messagebox.showinfo("Information", "Downloading the file, please wait...")
            dates = APItoXML.start(a)
            messagebox.showinfo("Information", "File download done.")
            XMLtoCSV.start(dates, self.share_select)
            CSVtoExcel.start()
        else:
            print("Disagree")

    def share_value(self, value):
        self.share_select = value

    def option_value(self, value):
        self.option_select = value

    def createButtonRow(self):
        b = Button(root, text="Download", command=self.helloCallBack)
        b.grid(row=3, column=0, columnspan=2)



root = tk.Tk()
app = GUI(master=root)
app.mainloop()
