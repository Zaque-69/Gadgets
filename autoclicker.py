from tkinter import *
from tkinter import messagebox
import pyautogui as auto
import time
import keyboard
import customtkinter
from PIL import Image, ImageTk

def page_2():
    class autoc:
        def __init__(self, master):
            self.master = master
            self.credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="gray", fg = "white", font=("Arial", 10, )).place(x=40, y=490)
            #img = PhotoImage(file="assets/bg_image/mouse.png", master = root)
            #self.lbl = Label(master, image = img, borderwidth=0)
            #self.lbl.image = img
            self.title = Label(master, text="Auto clicker", bg="gray", font=("Arial", 12), fg = "white").pack()
            self.milis = Label(master, text="Clicks:", background="gray",  fg = "white").place(x = 140, y = 80)
            self.space7 = Label(root, text="Interval between clicks:", bg="gray", fg = "white").place(x = 100, y = 130)
            #self.lbl.place(x = 80, y = 200)
            self.button1 = customtkinter.CTkButton(master, height = 30, width = 50, fg_color=("white"),border_width=1, command = self.cc, border_color="black", corner_radius=8,text_color="black",text = "Left", hover_color="silver").place(x=90, y=350)
            self.button2 = customtkinter.CTkButton(master, height = 30, width = 50, fg_color=("white"),border_width=1, command = self.clicks2, border_color="black", corner_radius=8,text_color="black",text = "Right", hover_color="silver").place(x=170, y=350)
            self.button3 = customtkinter.CTkButton(master, height = 30, width = 50, fg_color=("white"),border_width=1, command = self.whileTrue, border_color="black", corner_radius=8,text_color="black",text = "Countless", hover_color="silver").place(x = 118, y = 410)
   
            self.inputmilliseconds = Entry(root, width=30)
            self.inputmilliseconds.place(x = 70, y = 100)
            self.inputmilliseconds2 = Entry(root, width=30)
            self.inputmilliseconds2.place(x = 70, y = 150)
   
        def cc(self):

            INPUT = self.inputmilliseconds.get()
            INUPT2 = self.inputmilliseconds2.get()
            time.sleep(1)
            auto.click(button='left', clicks=int(INPUT), interval=float(INUPT2))
            messagebox.showinfo("Gadgets - Info!", "Succes")
           
               
        def whileTrue(self):
            x = True
            time.sleep(1)
            while x:
                auto.click(button="left")
                time.sleep(1)
                if keyboard.is_pressed('esc'):
                    messagebox.showinfo("Gadgets - Info!", "Succes")
                    break
            
        def clicks2(self):
            INPUT = self.inputmilliseconds.get()
            INUPT2 = self.inputmilliseconds2.get()
            time.sleep(1)
            auto.click(button='right', clicks=int(INPUT), interval=float(INUPT2))
            messagebox.showinfo("Gadgets - Info!", "Succes")
        
    root = Tk()

    root.geometry("320x520")
    root.title("Auto Clicker")
    root.configure(bg="gray")
    root.config(cursor="top_left_arrow")
    root.wm_attributes('-toolwindow', 'True')
    
    ex = autoc(root)

    if __name__=="__main__":
        mainloop()