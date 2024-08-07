from tkinter import *
import customtkinter
import pathlib as path
import shutil
from tkinter import messagebox, filedialog
import os    

aux = []
mainloc = os.getcwd()
with open ( "Files/test.in", "r") as ex:
    content = ex.read()
    for file2 in content.split(" "):
        aux.append(file2)

def page_5():
            
    class filem:
        def __init__(self, master):
            self.master = master
            self.space = Label(master, text="", bg="#8b4dff").pack()
            self.tt = Label(master, text="Organize Files with Python", fg="white", bg="#8b4dff",font=(12)).pack()
            self.space1 = Label(master, text="", bg="#8b4dff").pack()
            self.txt = Label(master, text="Please insert your location:", fg="white", bg="#8b4dff").pack()
            self.space2 = Label(master, text="", bg="#8b4dff").pack()
            self.credits = Label(master, bg = "#8b4dff", text="© 2023 Z4que ALL RIGHTS RESERVED", fg = "white", font = 10).place(x = 20, y = 220)
            self.btn = customtkinter.CTkButton(master, height=30, width=30, text="   Run   ", fg_color="#cfb5ff", hover_color="#e1d1ff", command = self.org, border_width=1, corner_radius=5, text_color="black").place(x = 340, y = 155)
            self.btn2 = customtkinter.CTkButton(master, height=30, width=30, text="Location", fg_color="#cfb5ff", hover_color="#e1d1ff", command = self.changedir, border_width=1, corner_radius=5, text_color="black").place(x = 400, y = 155)
            self.btn3 = customtkinter.CTkButton(master, height=30, width=30, text="  Add  ", fg_color="#cfb5ff", hover_color="#e1d1ff", command = self.addList, border_width=1, corner_radius=5, text_color="black").place(x = 340, y = 105)
            self.btn4 = customtkinter.CTkButton(master, height=30, width=30, text="  Delete  ", fg_color="#cfb5ff", hover_color="#e1d1ff", command = self.delete, border_width=1, corner_radius=5, text_color="black").place(x = 400, y = 105)
        
            self.inputtxt = Entry(root, width=40)
            self.inputtxt.place(x = 70, y = 110)
            #self.inputtxt2 = Entry(root, width=40)
            #self.inputtxt2.place(x = 70, y = 160)
        
        #change dirrectory
        def changedir(self):
            global aux
            
            loc = filedialog.askdirectory()
            print(aux) 
            if "//" in loc:
                pass
            else:
                loc = loc.replace("/", "//")
            os.chdir(loc) 
            
        #add 
        def addList(self):
            INPUT = self.inputtxt.get()
            
            with open( "Files/test.in", "a") as file:
                file.write(INPUT + " ")
            print("succes!")

        #main
        def org(self):   
            global aux
                
            del aux[-1]
            print(aux)
            for file2 in aux:
                os.mkdir(file2)
            
            for i in os.listdir():
                for file in aux:
                    if (file in i[-6:]):
                        shutil.move(i, file)
            messagebox.showinfo("Info!", "Succes!")

        def delete(self):
            INPUT = self.inputtxt.get()
            global mainloc
            global aux
            file3 = open( "Files/test.in", "r+" )
            file3.truncate(0)
            file3.close()

    root = Tk()
    root.geometry("500x250")
    root.configure(bg = "#8b4dff")
    root.config(cursor = "top_left_arrow")
    root.wm_attributes('-toolwindow', 'True')
    root.title("Organize your files")
    
    
    a = filem(root)

    if __name__=="__main__":
        root.mainloop()