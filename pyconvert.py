import time
import os
from tkinter import messagebox, filedialog
from tkinter import *
import customtkinter

def page_8():  

    ex = ""
    
    def open():
        global ex
        
        file = filedialog.askopenfilename()
        ex = file
        print(ex)        
        
    def convert():
        INPUT = input.get()
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
    
    sp = Label(root, text=" ", background="silver").pack()
    title = Label(root, text="Convert PY to EXE", bg="silver", font=(16), fg = "white").pack()
    input = Entry(root, width=50)
    input.pack()
    
    button = customtkinter.CTkButton(root, width=50, height=30, command = convert, text="Convert", fg_color="#e1e2e3", hover_color="#ffffff", border_color="black", border_width=1, text_color="black").place(x = 160, y = 90)
    button2 = customtkinter.CTkButton(root, width=50, height=30, command = open, text="Select File", fg_color="#e1e2e3", hover_color="#ffffff", border_color="black", border_width=1, text_color="black").place(x = 240, y = 90)
    space2 = Label(root, text=" ", background="silver").pack()
    credits = Label(root, text="© 2023 Z4que ALL RIGHTS RESERVED", background="silver", font=("Arial", 10, )).place(x=20, y=175)
    
    if __name__=="__main__":
        root.mainloop()