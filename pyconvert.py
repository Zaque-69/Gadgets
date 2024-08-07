import time
import os
from tkinter import messagebox, filedialog
from tkinter import *
import customtkinter

ex = ""

def page_8():  
    class convp:
        def __init__(self, master):
            self.master = master
            self.sp = Label(master, text=" ", background="silver").pack()
            self.title = Label(master, text="Convert PY to EXE", bg="silver", font=(16), fg = "white").pack()
            self.input = Entry(master, width=50)
            self.input.pack()
            
            self.button = customtkinter.CTkButton(master, width=50, height=30, command = self.convert, text="Convert", fg_color="#e1e2e3", hover_color="#ffffff", border_color="black", border_width=1, text_color="black").place(x = 160, y = 90)
            self.button2 = customtkinter.CTkButton(master, width=50, height=30, command = self.open, text="Select File", fg_color="#e1e2e3", hover_color="#ffffff", border_color="black", border_width=1, text_color="black").place(x = 240, y = 90)
            self.space2 = Label(master, text=" ", background="silver").pack()
            self.credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="silver", font=("Arial", 10, )).place(x=20, y=175)
    
        def open(self):
            global ex
            
            file = filedialog.askopenfilename()
            ex = file
            print(ex)        
            
        def convert(self):
            INPUT = self.input.get()
            print(INPUT)
            try:
                os.system(f'pyinstaller --onefile "{INPUT}"')
                time.sleep(0.2)
                print("Succes!") 
            except:
                os.system(f'pyinstaller --onefile "{ex}"')
                time.sleep(0.2)
                print("Succes!") 
    
    root = Tk()
    root.wm_attributes('-toolwindow', 'True')
    root.geometry("500x200")
    root.resizable(False, False)
    root.title("Convert PY to EXE")
    root.configure(bg="silver")
    root.config(cursor = "top_left_arrow")
    
    ah = convp(root)
    
    if __name__=="__main__":
        root.mainloop()