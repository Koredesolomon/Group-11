from tkinter import*
import tkinter as tk
from tkinter import ttk
from db.subject import get_subjects
from db.result import get_results

LARGEFONT =("Verdana", 20)
  
# label text for title
class StudentStats(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent,bg="Gold")

        button2 = ttk.Button(self, text ="Return to Home Page", 
        command = lambda : controller.backButton())
        button2.grid(row = 0, column = 0, padx = 10, pady = 10)

        ttk.Label(self, text = "Stats Table", 
                background = 'darkblue', foreground ="white", 
                font = LARGEFONT).grid(row = 1, column = 1)
        
        # label
        ttk.Label(self, text = "Select subject :",
                font = LARGEFONT).grid(column = 0,
                row = 5, padx = 10, pady = 25)
        
            # Combobox creation
        n = tk.StringVar()
        self.sub_combo = ttk.Combobox(self, width = 20, textvariable = n, postcommand=self.update_subjects)
        self.sub_combo.bind('<<ComboboxSelected>>', self.update_table)
            
            # Adding combobox drop down list
        subjects = get_subjects()
        self.sub_combo['values'] = tuple(subjects)

            
        self.sub_combo.grid(column = 1, row = 5)
        self.sub_combo.current()


        listData = [
                ("SN","firstname", "lastname", "matricno", "score")
                ]

        totalrow = len(listData)
        totalcolumn = len(listData[0])
        for i in range(totalrow):
                for j in range(totalcolumn):
                        self.e = ttk.Entry(self)
                        self.e.grid(row=i+6,column=j)
                        self.e.insert(END, listData[i][j])
                        self.e.config(state="readonly")

    def update_table(self, data):
        results = get_results(self.sub_combo.get())
        totalrow = len(results)
        totalcolumn = len(results[0])+1
        print(results)
        for i in range(totalrow):
                for j in range(totalcolumn):
                        self.e = ttk.Entry(self)
                        self.e.grid(row=i+7,column=j)
                        if (j == 0):
                                self.e.insert(END, (i*j)+1)
                        else:
                                self.e.insert(END, results[i][j-1])
                        self.e.config(state="readonly")

    def update_subjects(self):
        list = get_subjects()
        self.sub_combo['values'] = list