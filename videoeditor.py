from tkinter import filedialog, messagebox
from tkinter import *
import customtkinter
from moviepy.editor import VideoFileClip
import shutil
import os
import random
import numpy as np
from PIL import Image, ImageTk
import cv2

ex = ''
lol = os.getcwd()
giff = "Gif"

def page_10():
    class videoe:
        def __init__(self, master): 
            self.master = master
            self.name = Entry(root, width=30, bg="ivory")
            self.name.place(x = 50, y = 100)
            self.fpsrate = Entry(root, width=6, bg="ivory")
            self.fpsrate.place(x = 50, y = 160)

            self.Display = customtkinter.CTkButton(root, height=30, width=50, text="Gif", command = self.conv, border_width=1, corner_radius=5, fg_color="#8c6c74", hover_color="#bf959f").place(x = 260, y = 90)
            self.Display2 = customtkinter.CTkButton(root, height=30, width=50, text="Select File", command = self.open, border_width=1, corner_radius=5, fg_color="#8c6c74", hover_color="#bf959f").place(x = 110, y = 210)
            self.Display3 = customtkinter.CTkButton(root, height=30, width=55, text="  Mp3  ", command = self.Mp3, border_width=1, corner_radius=5, fg_color="#8c6c74", hover_color="#bf959f").place(x = 260, y = 150)
            
            self.credits = Label(root, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#57252e", fg="white", font=("Arial", 10, )).place(x=20, y=290)
            self.space1 = Label(root, text = " ", bg = "#57252e").pack()
            self.title = Label(root, text="Convert MP4 to GIF!", background="#57252e", fg="white", font=(12)).pack()
            self.space4 = Label(root, text=" ", background="#57252e").pack()
            self.space = Label(root, text = "Save as...", bg="#57252e", fg="white").place(x = 120, y = 70)
            self.space = Label(root, text = "Fps Rate", bg="#57252e", fg="white").place(x = 45, y = 130)
            self.onlyfps = Label(root, bg="#57252e", fg="white", text = "(Gif)").place(x = 55, y = 185)
            
            
        def conv (self):
            global ex
            NAME = self.name.get()
            FPSRATE = self.fpsrate.get()
            
            for filee in os.listdir():
                if not os.path.exists(giff):
                    os.mkdir(giff)
                else:  
                    pass
            try:
                if ex[-3:] == "mp4":
                    clip = VideoFileClip(ex)
                    clip.write_gif(NAME + ".gif", int(FPSRATE))
                    messagebox.showinfo("Info!", "Download Completed!")
                else:
                    messagebox.showerror("Info!", "Please insert an mp4 file!")
                    
                for filex in os.listdir():
                    if filex[-4:]==".gif":
                        shutil.move(filex, giff) 
            except:
                messagebox.showerror("Info!", "All fields are mandatory!")
        
        def Mp3(self):
            global ex
            lst = []
            for file in os.listdir():
                if (file == "Mp3"):
                    lst.append(file)
            if (len(lst) == 0):
                os.mkdir("Mp3")
            NAME = self.name.get()
            if (len(NAME) == 0):
                NAME = random.randint(1, 100000)
                
            clip = VideoFileClip(ex)
            audio = clip.audio
            audio.write_audiofile(str(NAME) + ".mp3")
            shutil.move(str(NAME) + ".mp3", "Mp3")
            messagebox.showinfo("Info!", "Download Completed!")
        
        def open(self):
            global ex
            
            file = filedialog.askopenfilename()
            ex = file
            print(ex)
   
    root = Tk()
    root.wm_attributes('-toolwindow', 'True')
    root.geometry("600x320")
    root.title("Video Editor")
    root.resizable(False, False)
    root.configure(bg = '#57252e')
    root.config(cursor="top_left_arrow")
    
    ah = videoe(root)
      
    if __name__=="__main__":    
        root.mainloop()   