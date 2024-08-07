from tkinter import *
from tkinter import messagebox
import cv2
import customtkinter
import qrcode
import os
from PIL import Image, ImageTk

def page_7():
    lol = os.getcwd()
    class qrc:
        def __init__(self, master):
            self.master = master
            self.space = Label(master, text="", bg="skyblue").pack()
            self.title = Label(master, bg="skyblue", text="QR Code Generator", font=(15)).pack()
            self.link = Label(master,text='Link',font = (15),bg='skyblue').place(x=70, y=80)
            self.saveas = Label(master,text='Save as',font = (15),bg='skyblue').place(x=55, y=110)
           
            self.btn = customtkinter.CTkButton(master, text='Generate QR code',command=self.generate, fg_color="lightblue", hover_color="#bfe4ff", border_color="black", border_width=1, corner_radius=5, text_color="black")
            self.btn.place(x=140, y=155)
            self.credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="skyblue", font=("Arial", 10, ))
            self.credits.place(x=20, y=470)
            
            self.msg = Entry(root, width = 35)
            self.msg.place(x=120, y=80)
            self.save_name = Entry(root, width = 35)
            self.save_name.place(x=120, y=110)
            
            self.label1 = Label(root, bg = "skyblue")
            self.label1.place(x=105, y=230)
            
            self.label2 = Label(root, bg="lightgray", relief = "ridge", width = 27, height = 12)
            self.label2.place(x=110, y=230)
            
        def generate(self):
            qrdir = "QR_CODE"
            input = self.msg.get()
            img = qrcode.make(str(input))
            type(img) 
            save = self.save_name.get()
            img.thumbnail((200, 200))
            img.save(f'{save}.jpg')
            
            fin = save + ".jpg"
            self.label2.destroy()
            
            image2 = PhotoImage(file = fin , master = root)
            self.label1.configure( image = image2 )
            self.label1.image = image2
            messagebox.showinfo("Info!", "Succes!")
                
    root = Tk()
    root.wm_attributes('-toolwindow', 'True')
    root.title('Qr Generator')
    root.geometry('400x500')
    root.resizable(False, False)
    root.config(bg='skyblue')
        
    ah = qrc(root)
    if __name__=="__main__":
        root.mainloop()