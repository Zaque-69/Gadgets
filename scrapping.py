from tkinter import messagebox
import requests
from bs4 import BeautifulSoup   
import os
import sys
from urllib.parse import urljoin
import customtkinter

def page_9():
	def scrap():
		
		def soupfindAllnSave(pagefolder, url, soup, tag2find='img', inner='src'):
			if not os.path.exists(pagefolder): 
				os.mkdir(pagefolder)
			for i in soup.findAll(tag2find):
				try:
					filename = os.path.basename(i[inner])  
					fileurl = urljoin(url, i.get(inner))
					filepath = os.path.join(pagefolder, filename)
					i[inner] = os.path.join(os.path.basename(pagefolder), filename)
					if not os.path.isfile(filepath):
						with open(filepath, 'wb') as file:
							filebin = session.get(fileurl)
							file.write(filebin.content)
				except Exception as exc:      
					print(exc, file=sys.stderr)
			return soup

		def savePage(response, pagefilename='page'):    
			url = response.url
			soup = BeautifulSoup(response.text)
			pagefolder = pagefilename+'_files'
			soup = soupfindAllnSave(pagefolder, url, soup, 'img', inner='src')
			soup = soupfindAllnSave(pagefolder, url, soup, 'link', inner='href')
			soup = soupfindAllnSave(pagefolder, url, soup, 'script', inner='src')    
			with open(pagefilename+'.html', 'w') as file:
				file.write(soup.prettify())
		 
			return soup
			
		INPUT = inputtxt.get()
		
		session = requests.Session()
		response = session.get(str(INPUT))
		savePage(response)
		
	root = Tk()
	root.geometry("500x230")
	root.configure(bg="#039389")
	root.config(cursor = "top_left_arrow")
	root.wm_attributes('-toolwindow', 'True')
	root.resizable(False, False)
	root.title("Web Scraping")
	
	space = Label(root, text="", bg="#039389").pack()
	title = Label(root, bg="#039389", text="Web Scraping", font=(15), fg="white").pack()
	pls = Label(root, text="Please insert your link:", bg="#039389", fg="white").pack()
	space1 = Label(root, text="", bg="#039389").pack()
	inputtxt = Entry(root, width = 50)
	inputtxt.pack()
	space2 = Label(root, text="", bg="#039389").pack()
	Btn = customtkinter.CTkButton(root, width=60, height=30, text="Run", fg_color="#007366", hover_color="#015A50", text_color="white", border_width=1, corner_radius=5, border_color="white", command=scrap).pack()
	credits = Label(root, bg="#039389", text="© 2023 Z4que ALL RIGHTS RESERVED", fg="white").place(x=20, y=200)
	
	root.mainloop()