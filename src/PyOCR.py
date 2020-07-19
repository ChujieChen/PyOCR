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
        master.geometry("1080x720")
        
        # Image display with Canvas
        self.canvas = Canvas(master, width=512, height=512, borderwidth=0, highlightthickness=0)
        path = self.preProcessImg(ifile='buzz.png')
        self.image = ImageTk.PhotoImage(path)
        self.image_on_canvas = self.canvas.create_image(0, 0, image=self.image, anchor=NW)
        
        # Canvas with selection
        self.rectCoords = [0, 0, 0, 0]
        topx, topy, topx, topy = self.rectCoords
        self.rect_id = self.canvas.create_rectangle(topx, topy, topx, topy,
                                  dash=(4,4), fill='', outline='red',width=2.0)
        self.canvas.bind('<Button-1>', self.get_mouse_posn)
        self.canvas.bind('<B1-Motion>', self.update_sel_rect)
        
        # Select Image - OCR
        browseBtn = Button(master, text='Browse', command=self.choose)
        choose = Label(master, text="Choose file")
        # self.image = PhotoImage(file='buzz.png')
        quit_btn = Button(master, text="Quit", command=self.quit_tool)
        # Output from OCR
        self.textBox = Text(self.master, height=50, width=30)
        self.textBox.insert(END, "NO TEXT FOR NOW")
        # Input for Homophones
        wordLable = Label(master, text="Type a word to get its homographs / homophones: ")
        self.word = StringVar(master)
        word_entry = Entry(master, textvariable=self.word,width=30)
        wordBtn = Button(master, text="Confirm", command=self.getHomo)
        # Output of homophones
        homoLable = Label(master, text="Candidates: ")
        self.homoBox = Text(master, height=10, width=30)
        self.homoBox.insert(END, "Ready to display some candidates!")
        
        ###### Layout ######
        row=0
        # self.inImg.grid(row=row, column=0, columnspan=2, rowspan=3)
        self.canvas.grid(row=row, column=0, columnspan=2, rowspan=3)
        
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
        
    
    def get_mouse_posn(self, event):
        # topx, topy
        self.rectCoords[0], self.rectCoords[1] = event.x, event.y

    def update_sel_rect(self, event):
        # botx, boty
        self.rectCoords[2], self.rectCoords[3] = event.x, event.y
        topx, topy, botx, boty = self.rectCoords
        self.canvas.coords(self.rect_id, topx, topy, botx, boty)  # Update selection rect.
    
    def getHomo(self):
        # has to be lowercase
        word = self.word.get().lower()
        homo_list = Word2Homo(word).getCandidates()
        self.homoBox.delete('1.0', END)
        for homo in homo_list:
            self.homoBox.insert(END, homo)
            self.homoBox.insert(END, "\n")
        
        
    def quit_tool(self):
        self.master.destroy()
        
    def choose(self):
        ifile = filedialog.askopenfile(parent=self.master,mode='rb',title='Choose a file')
        path = self.preProcessImg(ifile)
        self.image2 = ImageTk.PhotoImage(path)
        self.canvas.itemconfig(self.image_on_canvas, image=self.image2)
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, Img2Text(path).get_text())
    
    def preProcessImg(self, ifile):
        path = Image.open(ifile)
        width, height = path.size
        # fix size to 512 x 512
        newsize = (512, 512) 
        path = path.resize(newsize)
        return path
        
        
if __name__ == "__main__":
    root = Tk()
    gui = PyOCR(root)
    root.mainloop()