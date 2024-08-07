from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup   
import os
import sys
from urllib.parse import urljoin
import customtkinter

def page_9():
    class scrap:
        def __init__(self, master):
            self.master = master
            self.space = Label(master, text="", bg="#039389").pack()
            self.title = Label(master, bg="#039389", text="Web Scraping", font=(15), fg="white").pack()
            self.pls = Label(master, text="Please insert your link:", bg="#039389", fg="white").pack()
            self.space1 = Label(master, text="", bg="#039389").pack()
            self.inputtxt = Entry(master, width = 50)
            self.inputtxt.pack()
            self.space2 = Label(master, bg="#039389", text = "").pack()
            self.Btn = customtkinter.CTkButton(master, width=60, height=30, text="Run", fg_color="#007366", hover_color="#015A50", text_color="white", border_width=1, corner_radius=5, border_color="white", command = self.scrap).pack()
            self.credit = Label(master, bg="#039389", text="© 2023 Z4que ALL RIGHTS RESERVED", fg="white").place(x=20, y=200)

        def scrap(self):
            INPUT = self.inputtxt.get()
            gt = requests.get(str(INPUT))
            with open("html_code.txt", "w") as file:
                    file.write(str(gt.text))
            print(gt.text)
            messagebox.showinfo("Info!", "Succes!")
                    
    root = Tk()
    root.geometry("500x230")
    root.configure(bg="#039389")
    root.config(cursor = "top_left_arrow")
    root.wm_attributes('-toolwindow', 'True')
    root.resizable(False, False)
    root.title("Web Scraping")
    ah = scrap(root)
            
    if __name__ == "__main__":
            root.mainloop()
    
