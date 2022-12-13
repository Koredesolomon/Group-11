import tkinter as tk
from tkinter import ttk
from db.subject import init
from db.subject import get_subjects

import LandingPage 

import CreateSubject

import Result

import Stats

import StudentStats

LandingPage = LandingPage.LandingPage

CreateSubject = CreateSubject.CreateSubject

Result = Result.Result

Stats = Stats.Stats

StudentStats = StudentStats.StudentStats


  
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):

     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        

        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight =1)

        init()
        
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LandingPage, CreateSubject, Result, Stats, StudentStats):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew",)
  
        self.show_frame(LandingPage)

        
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def backButton(self):
        self.show_frame(LandingPage)


# Driver Code
app = tkinterApp()
app.mainloop()
  