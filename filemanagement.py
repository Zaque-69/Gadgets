from tkinter import *
import customtkinter
import pathlib as path
import shutil, os
from tkinter import messagebox

def page_5():
        
    def org():
        INPUT = inputtxt.get()
        if INPUT[len(INPUT)-1] != '/' : 
            INPUT += '/'

        extensions = []
        files = []
        folders_created = []

        dot = 0
        ext = ""
        for file in os.listdir(str(INPUT)):
            files.append(file)
            file += " "
            for c in range(0, len(file) - 1) : 
                if file[c] == '.' : 
                    dot = 1

                if dot == 1 and file[c + 1] != " ": 
                    ext += file[c + 1]
            extensions.append(ext)
            dot, ext = 0, ""
        
        for ext in extensions : 
            try : 
                os.mkdir(str(INPUT) + ext + "_files")
                folders_created.append(str(INPUT) + ext + "_files")
            except : 
                pass

        for ext in extensions : 
            for folder in folders_created :
                for file in files :  
                    if ext in file and ext in folder :  
                        try : 
                            shutil.move(str(INPUT) + file, folder)
                        except : pass

        messagebox.showinfo("Info!", "Succes!")
        
    root = Tk()
    root.geometry("500x200")
    root.configure(bg = "#8b4dff")
    root.config(cursor = "top_left_arrow")
    #root.wm_attributes('-toolwindow', 'True')
    root.title("Organize your files")
    
    space = Label(root, text="", bg="#8b4dff").pack()
    tt = Label(root, text="Organize Files with Python", fg="white", bg="#8b4dff",font=(12)).pack()
    space1 = Label(root, text="", bg="#8b4dff").pack()
    txt = Label(root, text="Please insert your location:", fg="white", bg="#8b4dff").pack()
    inputtxt = Entry(root, width=40)
    inputtxt.place(x = 70, y = 110)
    space2 = Label(root, text="", bg="#8b4dff").pack()
    btn = customtkinter.CTkButton(root, height=30, width=30, text="   Run   ", fg_color="#cfb5ff", hover_color="#e1d1ff", command=org, border_width=1, corner_radius=5, text_color="black").place(x = 340, y = 105)
    credits = Label(root, bg = "#8b4dff", text="© 2023 Z4que ALL RIGHTS RESERVED", fg = "white", font = 10).place(x = 20, y = 170)
    
    if __name__=="__main__":
        root.mainloop()