from tkinter import *
import random

root = Tk()
root.title('Color Game')
root.geometry('450x460')
root.config(bg = "#c1cbdb")
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)

class colorgame:
    def __init__(self, master):
        self.points = 0
        self.counter = 0
        self.cancel_id = None
        self.varcolor = ['blue', 'red', 'orange', 'yellow']
        self.varword = ['blue', 'red', 'orange', 'yellow']
        
        frame1 = Frame(root, bg='#6c7a70')
        frame1.pack(side=TOP)
        
        frame2 = Frame(root, bg='#424f45')
        frame2.pack()
        
        frame3 = Frame(root, bg='#6c7a70')
        frame3.pack()
        
        self.label1 = Label(frame1, text='Pick the box with matching text\nand background color\nFREE if there are no match\nGet as many points in 1 minute', bg='#6c7a70')
        self.label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)
        
        self.timer = Label(frame1, text=0, bg='#6c7a70')
        self.timer.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)
        
        self.pointslabel = Text(frame1, height=1, width=6, bg='#6c7a70', relief=FLAT)
        self.pointslabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)
        self.pointslabel.insert(END, 'Points:' + str(self.points))
        
        self.color1 = Button(frame2, text=self.varword[0], padx=20, pady=8, width=5, height=5, command=lambda: self.change(self.varcolor[0]))
        self.color1.grid(row=1, column=0, padx=10, pady=10, sticky=N+S+E+W)
        
        self.color2 = Button(frame2, text=self.varword[1], padx=20, pady=8, width=5, height=5, command=lambda: self.change(self.varcolor[1]))
        self.color2.grid(row=1, column=1, padx=10, pady=10, sticky=N+S+E+W)

        self.color3 = Button(frame2, text=self.varword[2], padx=20, pady=8, width=5, height=5, command=lambda: self.change(self.varcolor[2]))
        self.color3.grid(row=2, column=0, padx=10, pady=10, sticky=N+S+E+W)
        
        self.color4 = Button(frame2, text=self.varword[3], padx=20, pady=8, width=5, height=5, command=lambda: self.change(self.varcolor[3]))
        self.color4.grid(row=2, column=1, padx=10, pady=10, sticky=N+S+E+W)
        
        self.free = Button(frame2, text='FREE', padx=20, pady=20, bg='#9ea5b0',command=lambda: self.change('FREE'))
        self.free.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=N+S+E+W)
        
        self.button = Button(frame3, text='Start', padx=10, pady=10, command=self.startgame)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky=N+S+E+W)

        self.button2 = Button(frame3, text='Reset', padx=10, pady=10, command=self.reset)
        self.button2.grid(row=3, column=1, padx=10, pady=10, sticky=N+S+E+W)

        
    
    def change(self, answer):
        self.answer = answer
        
        if len(self.correctanswer) == 0:
            self.correctanswer.append('FREE')
        
        if self.answer in self.correctanswer:
            self.points += 1
            self.pointslabel.delete(1.0, END)
            self.pointslabel.insert(END, 'Points:' + str(self.points))
        
        word = ['blue', 'red', 'green', 'yellow']
        color =['blue', 'red', 'green', 'yellow']
        random.shuffle(word)
        random.shuffle(color)
        pair = {words: colors for words, colors in zip(word, color)}
        self.varword = list(pair.keys())
        self.varcolor = list(pair.values())
        self.correctanswer = []
        for i in range(0,4):
            if self.varword[i] == self.varcolor[i]:
                self.correctanswer.append(self.varword[i])
        self.color1.configure(text=self.varword[0], bg=self.varcolor[0])
        self.color2.configure(text=self.varword[1], bg=self.varcolor[1])
        self.color3.configure(text=self.varword[2], bg=self.varcolor[2])
        self.color4.configure(text=self.varword[3], bg=self.varcolor[3])  

    
    
    def startgame(self):
        word = ['blue', 'red', 'green', 'yellow']
        color =['blue', 'red', 'green', 'yellow']
        random.shuffle(word)
        random.shuffle(color)
        pair = {words: colors for words, colors in zip(word, color)}
        self.varword = list(pair.keys())
        self.varcolor = list(pair.values())
        self.correctanswer = []
        for i in range(0,4):
            if self.varword[i] == self.varcolor[i]:
                self.correctanswer.append(self.varword[i])
        self.color1.configure(text=self.varword[0], bg=self.varcolor[0])
        self.color2.configure(text=self.varword[1], bg=self.varcolor[1])
        self.color3.configure(text=self.varword[2], bg=self.varcolor[2])
        self.color4.configure(text=self.varword[3], bg=self.varcolor[3])
        self.countdown()
    
    def countdown(self):
        self.timer.configure(text=str(self.counter))
        self.cancel_id = root.after(1000, self.countdown)
        self.counter += 1
        if self.counter == 60:
            self.reset()    
    
    def stop(self):
        
        if self.cancel_id != None:
            self.timer.after_cancel(self.cancel_id)
            self.cancel_id = None

    def reset(self):
        self.endgame()
        self.stop()
        self.counter = 0
        self.timer.configure(text=str(self.counter))
        self.points = 0
        self.pointslabel.delete(1.0, END)
        self.color1.configure(bg='#9ea5b0')
        self.color2.configure(bg='#9ea5b0') 
        self.color3.configure(bg='#9ea5b0')
        self.color4.configure(bg='#9ea5b0')
        
    
    
    def endgame(self):
        self.top =Toplevel()
        self.top.title('Color Game')
        self.top.geometry('200x100')
        self.text2 = Text(self.top,)
        self.text2.insert(END, 'Thank you for Playing\nFinal Points:' + str(self.points))
        self.text2.pack()
    
    


e = colorgame(root)
root.mainloop()