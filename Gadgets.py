from tkinter import *
import time
import os
import customtkinter
from PIL import Image, ImageTk

import autoclicker
import spambot
import passworld
import filemanagement
import downloadyt
import qrgenerator
import pyconvert
import scrapping
import videoeditor
import photoeditor

class App:
    def __init__(self, master):
        self.master = master
        count = 0
        self.sp = Label(master, text=" ", bg="#383838").pack()
        self.title = Label(master, text="Welcome to GADGETS", bg="#383838", font=(15), fg="white").pack()
        self.Button1 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Auto Clicker", command = autoclicker.page_2, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=100, y=70)
        self.Button2 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Spam Bot", command = spambot.page_3, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=280, y=70)
        self.Button3 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Random", command = passworld.page_4, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=100, y=140)
        self.Button4 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="File Management", command = filemanagement.page_5, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=100, y=210)
        self.Button5 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Download YT Videos", command = downloadyt.page_6, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=280, y=140)
        self.Button6 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Qr Code Generator", command = qrgenerator.page_7, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=280, y=210)
        self.Button7 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="  Social ", command = self.main_pages, border_color="black", height=10, hover_color="#979797", corner_radius=4, text_color="black",width=30).place(x=20, y=15)
        self.Button9 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Shutdown", command = self.shutdown, border_color="black", height=10, hover_color="#979797", corner_radius=4, text_color="black", width=30).place(x=20, y=430)
        self.Button11 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Convert Py to EXE", command = pyconvert.page_8, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=100, y=280)
        self.Button12 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Web Scraping", command = scrapping.page_9, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=280, y=280)
        self.Button13 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Video Editor", command = videoeditor.page_10, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=100, y=350)
        self.Button14 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="Photo Editor", command=photoeditor.page_11, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black").place(x=280, y=350)
        self.credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#383838", font=("Arial", 10, ), fg = "white").place(x=270, y=445)
        self.Button14 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="System", command=self.systeminfo, border_color="black", height=10, hover_color="#979797", corner_radius=4, text_color="black", width=30).place(x=20, y=55)

        self.label1 = Label(master, text=" ", bg="#383838").place(x=460, y=50) 
        self.custom_button = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="+", command=self.clicked, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black", width=30)
        self.custom_button.place(x=440, y=70)
        self.custom_button1 = customtkinter.CTkButton(master, fg_color=("gray"),border_width=1, text="-", command=self.minus, border_color="black", height=37, hover_color="#979797", corner_radius=8, text_color="black", width=30)
        self.custom_button1.place(x=480, y=70)  

        self.labell =Label(root, bg="#383838", fg="white")
        self.labell.place(x=470, y=30)
        
    def main_pages(self):
        import webbrowser
        webbrowser.open_new("https://www.youtube.com/channel/UCj4LJSV016_F6OnBJJwRUTw")
        webbrowser.open_new("https://www.reddit.com/user/Z4queee")
        webbrowser.open_new("https://twitter.com/Z4queee")


    def shutdown(self):
        os.system("shutdown /s /t 0")
        
    def systeminfo(self):
        print(os.system(f"systeminfo"))
        time.sleep(1)
        print(os.system(f"ipconfig"))
        
    count = 0
    
    def clicked(self):
        global count
        count = count + 1
        self.labell.configure(text=str(count))
        return self.labell

    def minus(self):
        global count
        count = count - 1
        self.labell.configure(text=str(count))
        return self.labell
    
root = Tk()
count = 0
root.wm_attributes('-toolwindow', 'True')
root.resizable(False, False)
root.geometry("530x480")
root.configure(bg = "#383838")
root.title("Gagets")
root.config(cursor="top_left_arrow")

#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
#print(desktop)
my_guy = App(root)
os.system(f"color 3")
ok = 0
lol = os.getcwd() 

lst = []
for file in os.listdir():
    lst.append(file)
    if file == "Files":
        ok = 1

if ok == 0:
    os.mkdir("Files")
    os.chdir("Files")
    
    with open("zmvp.in", "w") as file1:
        pass
    with open("zmvp.out", "w") as file1:
        pass
        
os.chdir(lol)
print("""
                                                Welcome to
                                                
                              ▄████  ▄▄▄      ▓█████▄   ▄████ ▓█████▄▄▄█████▓  ██████ 
                             ██▒ ▀█▒▒████▄    ▒██▀ ██▌ ██▒ ▀█▒▓█   ▀▓  ██▒ ▓▒▒██    ▒ 
                            ▒██░▄▄▄░▒██  ▀█▄  ░██   █▌▒██░▄▄▄░▒███  ▒ ▓██░ ▒░░ ▓██▄   
                            ░▓█  ██▓░██▄▄▄▄██ ░▓█▄   ▌░▓█  ██▓▒▓█  ▄░ ▓██▓ ░   ▒   ██▒
                            ░▒▓███▀▒ ▓█   ▓██▒░▒████▓ ░▒▓███▀▒░▒████▒ ▒██▒ ░ ▒██████▒▒
                             ░▒   ▒  ▒▒   ▓▒█░ ▒▒▓  ▒  ░▒   ▒ ░░ ▒░ ░ ▒ ░░   ▒ ▒▓▒ ▒ ░
                              ░   ░   ▒   ▒▒ ░ ░ ▒  ▒   ░   ░  ░ ░  ░   ░    ░ ░▒  ░ ░
                            ░ ░   ░   ░   ▒    ░ ░  ░ ░ ░   ░    ░    ░      ░  ░  ░  
                                  ░       ░  ░   ░          ░    ░  ░              ░  
                                                             
                                          A new multi - tool APP 
                                          
                                                        © Z4que ALL RIGHTS RESERVED 2023
""")

mainloop()