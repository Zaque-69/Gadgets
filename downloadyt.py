from pytube import YouTube
from tkinter import messagebox
import os
import shutil
from tkinter import *
import customtkinter

def page_6():
    class download:
        def __init__(self, master):
            self.space1 = Label(master, text=" ", background="#80030f").pack()
            self.title = Label(master, text="Download YT videos. Please insert the link", background="#80030f", font=(12), fg="white").pack()
            self.space2 = Label(master, text=" ", background="#80030f").pack()
            self.Display = customtkinter.CTkButton(master, height=30, width=50, text="Download", command=self.main, fg_color="#fa6473", border_width=1, border_color="black", corner_radius=5, hover_color="#f7a6ae", text_color="black").place(x = 380, y = 85)
            self.credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#80030f", font=(10), fg="white").place(x=20, y=170)
            self.space4 = Label(master, text=" ", background="#80030f").pack()

        def main(self):
            ytpath = "Videos"
            INPUT = inputtxt.get()
            yt = YouTube(INPUT)
            try:
                ys = yt.get_highest_resolution()
                ys.download()
                
                messagebox.showinfo("Gadgets - Info!","Download completed!")
            except:
                messagebox.showinfo("Info!","You can't download private videos / videos that benefit the members of the respective channel!")    
                
    root = Tk()
    root.wm_attributes('-toolwindow', 'True')
    root.geometry("500x200")
    root.title("YT videos")
    root.resizable(False, False)
    root.configure(bg = '#80030f')
    root.config(cursor="top_left_arrow")
    
    inputtxt = Entry(root, width=50, bg="ivory")
    inputtxt.place(x = 40, y = 90)

    ex = download(root)
    
    if __name__=="__main__":    
        mainloop()