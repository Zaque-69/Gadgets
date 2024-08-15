from tkinter import *
import pyautogui as auto
import time
import keyboard
from tkinter import messagebox
import customtkinter

def page_3():
        

        def main():
            INSERT = inputtxt.get("1.0", "end-1c")
            MESS = mess.get("1.0", "end-1c")
            try:
                for i in range(int(MESS)+1):
                    if keyboard.is_pressed("esc"):
                        messagebox.showerror("Gadgets - Info!", "Succes!")
                        break
                    auto.write(INSERT)
                    auto.press("enter")
                    time.sleep(0.3)
                    if keyboard.is_pressed("esc"):
                        messagebox.showerror("Gadgets - Info!", "Succes!")
                        break
            except:
                messagebox.showerror("Info!", "You can't insert letters or negative numbers. Please try again!")
            
        def countless():
            INSERT = inputtxt.get("1.0", "end-1c")
            print(INSERT)
            time.sleep(2)
            while True:
                auto.write(INSERT)
                if keyboard.is_pressed("esc"):
                    messagebox.showerror("Gadgets - Info!", "Succes!")
                    break
                auto.press("enter")
                if keyboard.is_pressed("esc"):
                    messagebox.showerror("Gadgets - Info!", "Succes!")
                    break
                time.sleep(0.3)
                if keyboard.is_pressed("esc"):
                    messagebox.showerror("Gadgets - Info!", "Succes!")
                    break

        def textbox():
        
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
        print("                                     NOTICE! Tap -ESC- to stop the process!" )
        space = Label(root, text=" ", bg="#016b13")
        title = Label(root, text="Spam Bot", bg="#016b13", font=("Arial", 12), fg="white")
        ind = Label(root, bg="#016b13", text="Write the text here...", fg="white")
        inputtxt = Text(root, width=20, height=10)
        mess = Text(root, width=16, height=1)
        space1 = Label(root, text=" ", bg="#016b13")
        #customtkinter.CTkButton(root, height = 30, width = 50, fg_color=("white"),border_width=1, command=clicks2, border_color="black", corner_radius=8,text_color="black",text = "Right", hover_color="silver")
        press = customtkinter.CTkButton(root, height = 40, width = 70, fg_color=("#abf7c9"),border_width=1, command=main, border_color="black", corner_radius=8,text_color="black",text = " Run ", hover_color="#78f5aa")
        press3 = customtkinter.CTkButton(root, height = 40, width = 50, fg_color=("#abf7c9"),border_width=1, command=countless, border_color="black", corner_radius=8,text_color="black",text = "Countless", hover_color="#78f5aa")
        opentext = customtkinter.CTkButton(root, height = 20, width = 20, fg_color=("#abf7c9"),border_width=1, command=textbox, border_color="black", corner_radius=8,text_color="black",text = "Textbox", hover_color="#78f5aa")
        credits = Label(root, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#016b13", font=("Arial", 10), fg="white")

        space2 = Label(root, text=" ", bg="#016b13")
        space3 = Label(root, text=" ", bg="#016b13")

        credits.place(x=30, y=500)

        space.pack()
        title.pack()
        ind.pack()
        inputtxt.pack()
        space1.pack()
        txt = Label(root, text="Number of messages...", bg="#016b13", fg="white").pack()
        mess.pack()
        spacee = Label(root, text=" ", bg="#016b13").pack()
        press.pack()
        space10 = Label(root, text=" ", bg="#016b13").pack()
        
        press3.pack()
        space13= Label(root, text=" ", bg="#016b13").pack()
        opentext.pack()    
        
        if __name__=="__main__":      
            mainloop()