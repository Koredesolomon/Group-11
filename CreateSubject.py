import tkinter as tk
from tkinter import ttk, messagebox
from db.subject import create_subject


LARGEFONT =("Verdana", 20)

class CreateSubject(tk.Frame):
     
    def __init__(self, parent, controller,):

         
        tk.Frame.__init__(self, parent,bg="Gold")
        label = ttk.Label(self, text ="Enter Subject", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 50, pady = 10)

        self.entry_1 = ttk.Entry(self) 
        self.entry_1.grid(row = 1, column= 0, padx= 10, pady=10)

  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Create Subject", command=self.save_subject)
     
        # putting the button in its placee
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Return to Home Page",
        command = lambda : controller.backButton())
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

    def save_subject(self):
        try:
          create_subject(self.entry_1.get())
          self.entry_1.delete(0, 'end')
          messagebox.showinfo("Success", "Subject created successfully")
        except FileExistsError:
            messagebox.showerror("Error", "Subject already exists")
