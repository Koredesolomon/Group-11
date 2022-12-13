import tkinter as tk
from tkinter import ttk, messagebox
from db.subject import get_subjects
from db.result import save_result, result_exist
 
LARGEFONT =("Verdana", 10)

class Result(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent,bg="Gold")
        labl_0 = ttk.Label(self,text="Add Score",width=20, font = LARGEFONT,).grid(row = 0, column = 1, padx = 10, pady = 35)

        labl_1 = ttk.Label(self,text="First Name",width=10,foreground ="red", font = LARGEFONT).grid(row = 1, column = 0, padx =10, pady = 10)

        self.fn_entry = ttk.Entry(self) 
        self.fn_entry.grid(row = 1, column= 1, padx= 10, pady=10)

        labl_2 = ttk.Label(self,text="Last Name",width=20, foreground ="green", font = LARGEFONT).grid(row = 2, column = 0, padx = 50, pady = 10)

        self.ln_entry= ttk.Entry(self) 
        self.ln_entry.grid(row = 2, column= 1, padx= 10, pady=10)

        labl_3 = ttk.Label(self,text="Matric Number",width=20, foreground ="blue", font = LARGEFONT).grid(row = 3, column = 0, padx = 50, pady = 10)

        self.mat_entry = ttk.Entry(self) 
        self.mat_entry.grid(row = 3, column= 1, padx= 10, pady=10)

        labl_4 = ttk.Label(self,text="Score",width=20, foreground ="yellow", font = LARGEFONT).grid(row = 4, column = 0, padx = 50, pady = 10)

        self.res_entry = ttk.Entry(self) 
        self.res_entry.grid(row = 4, column= 1, padx= 10, pady=10)


        # label
        ttk.Label(self, text = "Select subject :",foreground ="violet",
                font = LARGEFONT).grid(column = 0,
                row = 5, padx = 10, pady = 25)

            # Combobox creation
        n = tk.StringVar()
        self.sub_combo = ttk.Combobox(self, width = 20, textvariable = n, postcommand=self.update_subjects)
            
            # Adding combobox drop down list
        subjects = get_subjects() 
        self.sub_combo['values'] = tuple(subjects)

            
        self.sub_combo.grid(column = 1, row = 5)
        self.sub_combo.current()  

        save_btn = ttk.Button(self, text ="Add Score", command= lambda : self.save_result())
     
        # putting the button in its place
        # by using grid
        save_btn.grid(row = 6, column = 0, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Return to Home Page", 
            command = lambda : controller.backButton())
        button2.grid(row = 7, column = 0, padx = 10, pady = 10)

    def update_subjects(self):
        list = get_subjects()
        self.sub_combo['values'] = list

    def reset_form(self):
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')
        self.mat_entry.delete(0, 'end')
        self.sub_combo.set('')
        self.res_entry.delete(0, 'end')
    
    def save_result(self):
        subjects = get_subjects()
        if self.sub_combo.get().lower() in subjects:
            messagebox.showwarning("Error", "Please choose a correct subject")
            return

        if len(self.fn_entry.get()) == 0 or len(self.ln_entry.get()) == 0 or len(self.mat_entry.get()) == 0 or len(self.res_entry.get()) ==0:
            messagebox.showwarning("Error", "Please fill in all the details")
            return

        if result_exist(self.sub_combo.get(), self.mat_entry.get()):
            messagebox.showwarning("Error", "Result has been recorded for this student")
            return

        if not self.res_entry.get().isdigit():
            messagebox.showwarning("Error", "Score must be a number")
            return

        if not self.mat_entry.get().isdigit():
            messagebox.showwarning("Error", "Matric Number must be a number")
            return

        if int(self.res_entry.get()) > 100:
            messagebox.showwarning("Error", "Score cannot be higher than 100")
            return

        if int(self.res_entry.get()) < 0:
            messagebox.showwarning("Error", "Score cannot be lower than 0")
            return

        if len(self.mat_entry.get()) != 9:
            messagebox.showwarning("Error", "Matric number must be 9 digits")
            return

        save_result(self.fn_entry.get(), self.ln_entry.get(),
         self.mat_entry.get(), self.sub_combo.get(),
         self.res_entry.get())

        messagebox.showinfo("Success", "Score saved") 

        self.reset_form()
    