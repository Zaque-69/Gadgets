from tkinter import *
import customtkinter
import pathlib as path
import shutil
from tkinter import messagebox

def page_5():
        
    def org():
        INPUT = inputtxt.get()
        if "//" in INPUT:
            pass
        else:
            INPUT = INPUT.replace("/", "//")
        os.chdir(str(INPUT))
        pypath = "Py-Pyw Files"
        htmlpath = "Html-Css-Js Files"
        photopath = "Photos"
        cpath = "C Files"
        vapath = "Mp3-Mp4 Files"
        zrpath = "Archive Files"
        docpath = "Document Files"
        pppath = "PowerPoint Files"
             
        for file in os.listdir():
            print(file)
            
            #for file in os.listdir():
            #print(file)
            #fisier = open("test.txt", "r")
            #liniifisier = fisier.read().splitlines()
            #for file in liniifisier:
                #if file.endswith(str(liniifisier)):
                    #os.mkdir(pypath)
                    #shutil.move(file, pypath)
            
            if file[-3:]==".py" or file[-4:] == "pyw":
                if not os.path.exists(pypath):
                    os.mkdir(pypath)
                    shutil.move(file, pypath)
                else:  
                    shutil.move(file, pypath)
                
            elif file[-5:] == ".html" or file[-4:] == ".css" or file[-3:] == ".js":
                if not os.path.exists(htmlpath):
                    os.mkdir(htmlpath)
                    shutil.move(file, htmlpath)
                else:  
                    shutil.move(file, htmlpath)
                    
            elif file[-5:] == ".jpeg" or file[-4:] == ".png" or file[-4:] == ".jpg" or file[-4:] == ".gif" or file[-4:]==".pdf":
                if not os.path.exists(photopath):
                    os.mkdir(photopath)
                    shutil.move(file, photopath)
                else:  
                    shutil.move(file, photopath)

            elif file[-4:] == ".cpp" or file[-3:] == ".cs" or file[-2:] == ".c":
                if not os.path.exists(cpath):
                    os.mkdir(cpath)
                    shutil.move(file, cpath)
                else:  
                    shutil.move(file, cpath)
                    
            elif file[-4:] == ".mp3" or file[-4:] == ".mp4":
                if not os.path.exists(vapath):
                    os.mkdir(vapath)
                    shutil.move(file, vapath)
                else:  
                    shutil.move(file, vapath)    
                    
            elif file[-4:] == ".zip" or file[-4:] == ".rar":
                if not os.path.exists(zrpath):
                    os.mkdir(zrpath)
                    shutil.move(file, zrpath)
                else:  
                    shutil.move(file, zrpath)  
                    
            elif file[-4:] == ".doc" or file[-5:] == ".docx":
                if not os.path.exists(docpath):
                    os.mkdir(docpath)
                    shutil.move(file, docpath)
                else:  
                    shutil.move(file, docpath) 
                    
            elif file[-5:] == ".pptx" or file[-4:] == ".ppt":
                if not os.path.exists(pppath):
                    os.mkdir(pppath)
                    shutil.move(file, pppath)
                else:  
                    shutil.move(file, pppath)      
                    
            else:
                pass
        messagebox.showinfo("Info!", "Succes!")
        
    root = Tk()
    root.geometry("500x200")
    root.configure(bg = "#8b4dff")
    root.config(cursor = "top_left_arrow")
    root.wm_attributes('-toolwindow', 'True')
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