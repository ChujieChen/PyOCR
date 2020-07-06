import os
from tkinter import *
from tkinter import filedialog
from PIL import  Image,ImageTk
from img2text import Img2Text
from word2homo import Word2Homo

class PyOCR:
    def __init__(self, master):
        self.master = master
        padx = 10
        pady = 10
        # Title
        master.title("PyOCR - Chujie Chen")
        master.geometry("1200x760")
        # Select Image - OCR
        browseBtn = Button(master, text='Browse', command=self.choose)
        choose = Label(master, text="Choose file")
        self.image = PhotoImage(file='buzz.png')
        self.inImg = Label(image=self.image)
        quit_btn = Button(master, text="Quit", command=self.quit_tool)
        # Output from OCR
        self.textBox = Text(self.master, height=50, width=30)
        self.textBox.insert(END, "NO TEXT FOR NOW")
        # Input for Homophones
        wordLable = Label(master, text="Type a word to get its homophones: ")
        self.word = StringVar(master)
        word_entry = Entry(master, textvariable=self.word)
        wordBtn = Button(master, text="Confirm", command=self.getHomo)
        # Output of homophones
        homoLable = Label(master, text="Homophones: ")
        self.homoBox = Text(master, height=10, width=30)
        self.homoBox.insert(END, "Ready to display some homophones")
        
        ###### Layout ######
        row=0
        self.inImg.grid(row=row, column=0, columnspan=2, rowspan=5)
        self.textBox.grid(row=row, column=2, rowspan=5)
        wordLable.grid(row=row, column=3)
        
        row=1
        word_entry.grid(row=row, column=3)
        
        row=2
        wordBtn.grid(row=row, column=3)
        
        row=3
        homoLable.grid(row=row, column=3)
        
        row=4
        choose.grid(row=row, column=0)
        browseBtn.grid(row=row, column=1)
        self.homoBox.grid(row=row, column=3, rowspan=2)
        
        row=5
        quit_btn.grid(row=row, column=1)
        
        
    def getHomo(self):
        homo_list = Word2Homo(self.word.get()).getHomophones()
        self.homoBox.delete('1.0', END)
        for homo in homo_list:
            self.homoBox.insert(END, homo)
            self.homoBox.insert(END, "\n")
        
        
    def quit_tool(self):
        self.master.destroy()
        
    def choose(self):
        ifile = filedialog.askopenfile(parent=self.master,mode='rb',title='Choose a file')
        path = Image.open(ifile)
    
        self.image2 = ImageTk.PhotoImage(path)
        self.inImg.configure(image=self.image2)
        self.inImg.image=self.image2
        
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, Img2Text(path).get_text())
        
        
        
if __name__ == "__main__":
    root = Tk()
    gui = PyOCR(root)
    root.mainloop()