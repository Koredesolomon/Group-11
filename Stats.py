import tkinter as tk
from tkinter import ttk
from db.subject import get_subjects
from db.result import get_highest
from db.result import get_mean
from db.result import get_above_count
from db.result import get_lowest


LARGEFONT =("Verdana", 20)
  
# label text for title
class Stats(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent,bg="Gold")
        ttk.Label(self, text = "Average Stats", 
                background = 'green', foreground ="white", 
                font = LARGEFONT).grid(row = 0, column = 1)
        
        # label
        ttk.Label(self, text = "Select subject :",
                font = LARGEFONT).grid(column = 0,
                row = 5, padx = 10, pady = 25)
        
        # Combobox creation
        n = tk.StringVar()
        self.sub_combo = ttk.Combobox(self, width = 20, textvariable = n, postcommand=self.update_subjects)
        self.sub_combo.bind('<<ComboboxSelected>>', self.update_score,)
        
        # Adding combobox drop down list
        subjects = get_subjects()
        self.sub_combo['values'] = tuple(subjects)

            
        self.sub_combo.grid(column = 1, row = 5)
        self.sub_combo.current()
        # self.mainloop()

        ttk.Label(self, text = "Highest Scoring Student",
                font = LARGEFONT).grid(column = 0,
                row = 6, padx = 10, pady = 25)

        ttk.Label(self, text = "Mean Score",
                font = LARGEFONT).grid(column = 0,
                row = 7, padx = 10, pady = 25)

        ttk.Label(self, text = "Students who scored above 70",
                font = LARGEFONT).grid(column = 0,
                row = 8, padx = 10, pady = 25)

        ttk.Label(self, text = "Lowest scoring student",
                font = LARGEFONT).grid(column = 0,
                row = 9, padx = 10, pady = 25)

        button2 = ttk.Button(self, text ="Return to Home Page", 
        command = lambda : controller.backButton())
        button2.grid(row = 10, column = 0, padx = 10, pady = 10)

    def update_score(self, data):
                highest = get_highest(self.sub_combo.get())
                self.e = ttk.Entry(self, width=40)
                self.e.grid(row=6,column=1)
                self.e.insert("end", highest)
                self.e.config(state="readonly")

                mean = get_mean(self.sub_combo.get())
                self.e = ttk.Entry(self, width=10)
                self.e.grid(row=7,column=1)
                self.e.insert('end', mean)
                self.e.config(state="readonly")

                count = get_above_count(self.sub_combo.get(), 70)
                self.e = ttk.Entry(self, width=40)
                self.e.grid(row=8,column=1)
                self.e.insert("end", count)
                self.e.config(state="readonly")

                lowest= get_lowest(self.sub_combo.get())
                self.e = ttk.Entry(self,width=30)
                self.e.grid(row=9,column=1)
                self.e.insert('end', lowest)
                self.e.config(state="readonly")

    def update_subjects(self):
        list = get_subjects()
        self.sub_combo['values'] = list
