from tkinter import *
import customtkinter
import random
from tkinter import messagebox 
import pyperclip

def page_4():

    class rand:
        def __init__(self, master):
            self.nrc = Label(master, bg="#f78707", text="Number of characters").place(x=115, y=55)
            self.genpas = customtkinter.CTkButton(master, text="Generate", fg_color="#faca93", hover_color="#fce6cc", border_width=1, corner_radius=5, width=30, text_color="black", command=self.passworld).place(x=110, y=120)
            self.delpass = customtkinter.CTkButton(master, text="Delete", fg_color="#faca93", hover_color="#fce6cc", border_width=1, corner_radius=5, width=30, text_color="black", command=self.deleteText2).place(x=190, y=120)
            self.bttpass = customtkinter.CTkButton(master, width=50, height=30, text="Copy Passworld", command = self.copy, border_width=1, corner_radius=5, fg_color="#faca93", hover_color="#fce6cc", text_color="black").place(x=120, y=172)

            self.credits = Label(master, text="© 2023 Z4que ALL RIGHTS RESERVED", background="#f78707", font=("Arial", 10, ))
            self.credits.place(x=330, y=350)
            self.tt = Label(master, text="Passworld Generator", background="#f78707", font=("Arial", 12)).place(x=100, y=20)
            
            self.space1 = Label(master, text=" ", background="#f78707").pack()
            self.space2 = Label(master, text=" ", background="#f78707").pack()
            self.space3 = Label(master, text=" ", background="#f78707").pack()
            self.space = Label(master, text=" ", background="#f78707").pack()
            
            self.label4 = Label(master, bg="#f78707",text="Tap the buttons to generate random numbers", font=("Arial", 12)).place(x=310, y=20)
            self.button = customtkinter.CTkButton(master, width=50, height=30, text="Generate", command = self.generate, border_width=1, corner_radius=5, fg_color="#faca93", hover_color="#fce6cc", text_color="black").place(x=505, y=162)
            self.delete = customtkinter.CTkButton(master, width=50, height=30, text="Delete", command = self.deleteText, border_width=1, corner_radius=5, fg_color="#faca93", hover_color="#fce6cc", text_color="black").place(x=512, y=197)
            
            self.txt1 = Label(master, text="Min. Number", bg="#f78707").place(x=437, y=55)
            self.txt2 = Label(master, text="Max. Number", bg="#f78707").place(x=437, y=105)
            self.txt3 = Label(master, text="How many" + "\n" +  "numbers", bg="#f78707").place(x=397, y=155)
            
            self.Outputpass = Text(root, height=6, width=30, bg="white")
            self.Outputpass.place(x=50, y=240)
            self.getpass = Entry(root, width=30)
            self.getpass.place(x=80, y=80)
            
            self.entry1 = Entry(root, width=30)
            self.entry2 = Entry(root, width=30)
            self.entry3 = Entry(root, width=15)
            self.entry1.place(x=380, y=80)
            self.entry2.place(x=380, y=130)
            self.entry3.place(x=380, y=200)
            
            self.Output = Text(root, height=6, width=30, bg="white")
            self.Output.place(x=350, y=240)   
                
        def deleteText(self):
            self.Output.delete("1.0", END)
                
        def deleteText2(self):
            self.Outputpass.delete("1.0", END)
            
        def passworld(self):
            import pyperclip
            from tkinter import messagebox
            
            pas = self.getpass.get()
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            print(len(string))
            if( int(pas) < 74):
                a = "".join(random.sample(string, k=(int(pas))))
                afin = a + "\n"
                self.Outputpass.insert(END, afin, "\n")
                print("da")
            else:
                p = 0
                fin = ""
                x = int(pas)/73
                print(int(x))
                for j in range(int(x)):
                    p += 73
                rest = int(pas) - p
                for i in range(int(x)):
                    b = "".join(random.sample(string, k = 73))
                    self.Outputpass.insert(END, b, "\n")
                c = "".join(random.sample(string, k = rest))
                self.Outputpass.insert(END, str(c) ,"\n")
                    
            
        def copy(self):
            ex = self.Outputpass.get("1.0", "end-1c")
            pyperclip.copy(ex)
            
        def generate(self):
            nrmin = self.entry1.get() 
            nrmax = self.entry2.get() 
            hmn = self.entry3.get() 
            try:
                if(int(nrmin) > int(nrmax)):
                    messagebox.showerror("Info!", "Minim Number can't be bigger than Maxim Number!")
                else:
                    try:
                        for i in range(int(hmn)):
                            number = random.randint(int(nrmin), int(nrmax))
                            x = str(number) + "\n"
                            self.Output.insert(END, str(x), "\n")
                    except:
                        messagebox.showerror("Info!", "You must insert numbers. Please try again!")
            except:
                messagebox.showerror("Info!", "All fields are mandatory!")
            
    root = Tk()
    root.wm_attributes('-toolwindow', 'True')
    root.geometry("660x380")
    root.resizable(False, False)
    root.title(" Random  ")
    root.configure(bg = "#f78707")
    root.config(cursor="top_left_arrow")
    
    ex = rand(root)
  
    if __name__=="__main__":
        mainloop()