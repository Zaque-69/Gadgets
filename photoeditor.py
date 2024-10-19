from tkinter import *
import customtkinter
import cv2
import os
import random
from tkinter import filedialog, messagebox

def page_11():
    class photoe:
        def __init__(self, master):
            self.space = Label(master, bg="#765ec4").pack()
            self.title = Label(master, bg="#765ec4", text = "Photo Editor", font=(12), fg="white").pack()
            self.ri = Label(master, text="Resize image", fg="white", bg="#765ec4").place(x=65, y=80)
            self.xpos = Label(master, bg="#765ec4", text="X", fg="white").place(x=40, y=110)
            self.ypos = Label(master, bg="#765ec4", text="Y", fg="white").place(x=40, y=140)
            self.btn = customtkinter.CTkButton(master, width=60, height=30, text="Resize", border_width=1, text_color="black", fg_color="#9684d1", hover_color="#a89bd4", border_color = "black", command = self.resizePhoto).place(x=180, y=105)
            self.select = customtkinter.CTkButton(master, width=60, height=30, text="Select", border_width=1, text_color="black", fg_color="#9684d1", hover_color="#a89bd4", border_color = "black", command = self.open).place(x=75, y=170)

            self.credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#765ec4", fg="white", font=("Arial", 10, )).place(x=20, y=290)
            
        ex = ''
        
        def open(self):
            global ex
            file = filedialog.askopenfilename()
            ex = file
            print(ex)
        
        def remove_bg(self):
            global ex
            
        def resizePhoto(self):
            global ex
            xsize = int(x.get())
            ysize = int(y.get())
            img = cv2.imread(ex)
            
            fin = cv2.resize(img, (int(xsize), int(ysize)))
            filename = random.randint(1, 10000)
            cv2.imwrite(str(filename) + ".jpg", fin)
            messagebox.showinfo("Info!", "Succes!")
        
    root = Tk()
    root.geometry("600x320")
    root.title("Photo Editor")
    root.wm_attributes("-toolwindow", "True")
    root.resizable("False", "False")
    root.configure(bg = "#765ec4")
    root.config(cursor = "top_left_arrow")
    
    x = Entry(root, width=15)
    x.place(x=60, y=110)
    y = Entry(root, width=15)
    y.place(x=60, y=140)
    
    e = photoe(root)
    
    if __name__ == "__main__":
        root.mainloop()