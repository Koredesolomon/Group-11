import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 20)

import CreateSubject

import Result

import Stats

import StudentStats

CreateSubject = CreateSubject.CreateSubject

Result = Result.Result

Stats = Stats.Stats

StudentStats = StudentStats.StudentStats

class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Gold")
                
        # label of frame Layout 2
        label = ttk.Label(self, text ="Landing page", font = LARGEFONT,foreground="darkblue")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Create Subject",
        command = lambda : controller.show_frame(CreateSubject))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Add Score",
        command = lambda : controller.show_frame(Result))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

        ## button to show frame 2 with text layout2
        button3 = ttk.Button(self, text ="Stats",
        command = lambda : controller.show_frame(Stats))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 2, column = 1, padx = 10, pady = 10)


        ## button to show frame 2 with text layout2
        button4 = ttk.Button(self, text ="Student Stats",
        command = lambda : controller.show_frame(StudentStats))
     
        # putting the button in its place by
        # using grid
        button4.grid(row = 2, column = 2, padx = 10, pady = 10)

