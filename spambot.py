from tkinter import *
import pyautogui as auto
import time
import keyboard
from tkinter import messagebox
import customtkinter
import sys

def page_3():
    class spamb:
        def __init__(self, master):
            self.master = master
            self.space = Label(master, text=" ", bg="#016b13").pack()
            self.title = Label(master, text="Spam Bot", bg="#016b13", font=("Arial", 12), fg="white").pack()
            self.ind = Label(master, bg="#016b13", text="Write the text here...", fg="white").pack()
            self.inputtxt = Text(master, width=20, height=10)
            self.inputtxt.pack()
            self.space1 = Label(master, text=" ", bg="#016b13").pack()
            self.txt = Label(master, text="Number of messages...", bg="#016b13", fg="white").pack()
            self.mess = Text(master, width=16, height=1)
            self.mess.pack()

            self.spacee = Label(master, text=" ", bg="#016b13").pack()
            self.press = customtkinter.CTkButton(master, height = 40, width = 70, fg_color=("#abf7c9"),border_width=1, command = self.main, border_color="black", corner_radius=8,text_color="black",text = "Run", hover_color="#78f5aa").pack()
            self.space10 = Label(master, text=" ", bg="#016b13").pack()
            self.press3 = customtkinter.CTkButton(master, height = 40, width = 50, fg_color=("#abf7c9"),border_width=1, command = self.countless, border_color="black", corner_radius=8,text_color="black",text = "Countless", hover_color="#78f5aa").pack()
            self.space13= Label(master, text=" ", bg="#016b13").pack()
            self.opentext = customtkinter.CTkButton(master, height = 40, width = 20, fg_color=("#abf7c9"),border_width=1, command = self.textbox, border_color="black", corner_radius=8,text_color="black",text = "Textbox", hover_color="#78f5aa").pack() 

            credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#016b13", font=("Arial", 10), fg="white").place(x=30, y=500)

        def exit():
            messagebox.showinfo("Info!", "Succes!")
            sys.exit()
            
        def main(self):
            INSERT = self.inputtxt.get("1.0", "end-1c")
            MESS = self.mess.get("1.0", "end-1c")
            try:
                for i in range(int(MESS)+1):
                    if keyboard.is_pressed("esc"):
                        exit()
                    auto.write(INSERT)
                    auto.press("enter")
                    time.sleep(0.3)
                    if keyboard.is_pressed("esc"):
                        exit()
            except:
                messagebox.showerror("Info!", "You can't insert letters or negative numbers. Please try again!")
            
        def countless(self):
            INSERT = self.inputtxt.get("1.0", "end-1c")
            print(INSERT)
            time.sleep(2)
            while True:
                auto.write(INSERT)
                if keyboard.is_pressed("esc"):
                    exit()
                auto.press("enter")
                if keyboard.is_pressed("esc"):
                    exit()
                time.sleep(0.3)
                if keyboard.is_pressed("esc"):
                    exit()

        def textbox(self):
        
            from tkinter import filedialog
            import customtkinter
            
            def save_as():
                file = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt")
                if file is None:
                    return
                txt = str(input.get(1.0, END))
                file.write(txt)
                file.close()
                
            def open_file():
                file = filedialog.askopenfile(mode = 'r')
                if file is not None:
                    content = file.read()
                input.insert(INSERT, content)    
                
                
            window = Tk()
            window.title("Textbox")
            window.wm_attributes("-toolwindow", "True")
            window.geometry("900x600")
            window.resizable(False, False)
            window.wm_attributes('-toolwindow', 'True')
            input = Text(window, height=1000, width=1000)
            nav = Label(window, bg="lightgray", height=3, width=1000).pack()
            btn1 = Button(window, height = 2, width = 8, bg=("lightgray"), text = "Save as", relief = "flat", command=save_as)
            btn1.place(x=30, y=7)
            btn2 = Button(window, height = 2, width = 8, bg=("lightgray"), text = "Open File", relief = "flat", command=open_file)
            btn2.place(x=150, y=7)
            input.pack()
            window.mainloop()
            
    root = Tk()
    root.wm_attributes('-toolwindow', 'True')
    root.geometry("300x540")
    root.resizable(False, False)
    root.title("Spam Bot")
    root.configure(bg="#016b13")
    root.config(cursor="top_left_arrow")

    ah = spamb(root)
    
    if __name__=="__main__":      
        mainloop()