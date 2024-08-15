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

def page_10():
    lol = os.getcwd()
    giff = "Gif"
    ex = ''
    
    def Take_input():
        global ex
        NAME = name.get()
        FPSRATE = fpsrate.get()
        
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
    
    def Mp3():
        global ex
        
        lst = []
        for file in os.listdir():
            if (file == "Mp3"):
                lst.append(file)
        if (len(lst) == 0):
            os.mkdir("Mp3")
        NAME = name.get()
        if (len(NAME) == 0):
            NAME = random.randint(1, 100000)
            
        clip = VideoFileClip(ex)
        audio = clip.audio
        audio.write_audiofile(str(NAME) + ".mp3")
        shutil.move(str(NAME) + ".mp3", "Mp3")
        messagebox.showinfo("Info!", "Download Completed!")
    
    def open():
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
  
    name = Entry(root, width=30, bg="ivory")
    fpsrate = Entry(root, width=6, bg="ivory")

    Display = customtkinter.CTkButton(root, height=30, width=50, text="Gif", command=Take_input, border_width=1, corner_radius=5, fg_color="#8c6c74", hover_color="#bf959f")
    Display2 = customtkinter.CTkButton(root, height=30, width=50, text="Select File", command=open, border_width=1, corner_radius=5, fg_color="#8c6c74", hover_color="#bf959f")
    Display3 = customtkinter.CTkButton(root, height=30, width=55, text="  Mp3  ", command=Mp3, border_width=1, corner_radius=5, fg_color="#8c6c74", hover_color="#bf959f")
    
    credits = Label(root, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#57252e", fg="white", font=("Arial", 10, )).place(x=20, y=290)
    space1 = Label(root, text = " ", bg = "#57252e").pack()
    title = Label(root, text="Convert MP4 to GIF!", background="#57252e", fg="white", font=(12)).pack()
    space4 = Label(root, text=" ", background="#57252e").pack()
    space = Label(root, text = "Save as...", bg="#57252e", fg="white").place(x = 120, y = 70)
    name.place(x = 50, y = 100)
    space = Label(root, text = "Fps Rate", bg="#57252e", fg="white").place(x = 45, y = 130)
    fpsrate.place(x = 50, y = 160)
    onlyfps = Label(root, bg="#57252e", fg="white", text = "(Gif)").place(x = 55, y = 185)
    
    Display.place(x = 260, y = 90)
    Display2.place(x = 110, y = 210)
    Display3.place(x = 260, y = 150)
      
    page()
    
    if __name__=="__main__":    
        root.mainloop()   