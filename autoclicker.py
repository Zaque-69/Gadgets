from tkinter import *
import pyautogui as auto
import time
import keyboard
import customtkinter
from PIL import Image, ImageTk

def page_2():
    def clicks():
        try:
            INPUT = inputmilliseconds.get("1.0", "end-1c")
            INUPT2 = inputmilliseconds2.get("1.0", "end-1c")
            time.sleep(1)
            auto.click(button='left', clicks=int(INPUT), interval=float(INUPT2))
            messagebox.showinfo("Gadgets - Info!", "Succes")
        except:
            messagebox.showerror("Info!", "You can't insert letters or negative numbers. Please try again!")
       
    def whileTrue():
        x = True
        time.sleep(1)
        while x:
            auto.click(button="left")
            time.sleep(30)
            if keyboard.is_pressed('esc'):
                messagebox.showinfo("Gadgets - Info!", "Succes")
                break
        
    def clicks2():
        try:
            INPUT = inputmilliseconds.get("1.0", "end-1c")
            INUPT2 = inputmilliseconds2.get("1.0", "end-1c")
            time.sleep(1)
            auto.click(button='right', clicks=int(INPUT), interval=float(INUPT2))
            messagebox.showinfo("Gadgets - Info!", "Succes")
        except:
            messagebox.showerror("Info!", "You can't insert letters or negative numbers. Please try again!")
     
    root = Tk()

    root.geometry("320x520")
    root.title("Auto Clicker")
    root.configure(bg="gray")
    root.config(cursor="top_left_arrow")
    
    space8 = Label(root, text=" ", bg="gray")
    space2 = Label(root, text=" ", bg="gray")
    space3 = Label(root, text=" ", bg="gray")
    button3 = customtkinter.CTkButton(root, height = 30, width = 50, fg_color=("white"),border_width=1, command=whileTrue, border_color="black", corner_radius=8,text_color="black",text = "Countless", hover_color="silver")
    space1 = Label(root, text=" ", bg="gray")
    credits = Label(root, text="© 2023 Z4que ALL RIGHTS RESERVED", background="gray", fg = "white", font=("Arial", 10, )).place(x=40, y=490)
  
    img = PhotoImage(file="assets/bg_image/mouse.png", master = root)
    lbl = Label(root, image = img, borderwidth=0)
    lbl.image = img
    
    space = Label(root, text=" ", bg="gray").pack()
    title = Label(root, text="Auto clicker", bg="gray", font=("Arial", 12)).pack()
    space5 = Label(root, text=" ", bg="gray").pack()
    milis = Label(root, text="Clicks:", background="gray").pack()
    inputmilliseconds = Text(root, height=1, width=25, background="white")
    inputmilliseconds.pack()
    sca = Label(root, text=" ", bg="gray").pack()
    space6 = Label(root, text="Interval between clicks:", bg="gray").pack()
    inputmilliseconds2 = Text(root, height=1, width=25, background="white").pack()
    scac = Label(root, text=" ", bg="gray").pack()
    scac = Label(root, text=" ", bg="gray").pack()
    lbl.pack()
    button1 = customtkinter.CTkButton(root, height = 30, width = 50, fg_color=("white"),border_width=1, command=clicks, border_color="black", corner_radius=8,text_color="black",text = "Left", hover_color="silver").place(x=92, y=350)
    button2 = customtkinter.CTkButton(root, height = 30, width = 50, fg_color=("white"),border_width=1, command=clicks2, border_color="black", corner_radius=8,text_color="black",text = "Right", hover_color="silver").place(x=172, y=350)
    space8.pack()
    space2.pack()
    space3.pack()
    button3.pack()
    space1.pack()
    
    if __name__=="__main__":
        mainloop()