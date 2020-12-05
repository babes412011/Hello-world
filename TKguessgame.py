# Number guessing game with difficulty level
from tkinter import *
import random
from tkinter import font as tkFont
num = random.randint(1,50)
root = Tk()
root.title('Guessing Game')
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)
root.geometry('250x300')
root.config(bg = "#242529")
helv36 = tkFont.Font(family='Helvetica', size=8, weight='bold')

class GuessGame:

    def change(self, max):
        self.maxnum = max
        self.var = ('Guess the number from 1 to ' + str(self.maxnum))
        self.reset()
        self.mylabel1.delete(1.0, END)
        self.mylabel1.insert(END, self.var)
        self.top.destroy()
    
    def level(self):
        self.top =Toplevel()
        self.top.title('Choose a Difficulty')
        self.top.geometry('200x100')
        self.top.config(bg = "#242529")
        
        self.Easy = Button(self.top, text='Easy', width=8, bg='#293040', font=helv36, command=lambda: self.change(30))
        self.Easy.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

        self.Medium = Button(self.top, text='Medium', width=8, bg='#293040', font=helv36,command=lambda: self.change(50))
        self.Medium.grid(row=0, column=1, padx=10, pady=10, sticky=N+S+E+W)

        self.Hard = Button(self.top, text='Hard', width=8, bg='#293040', font=helv36,command=lambda: self.change(70))
        self.Hard.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=N+S+E+W)
    
    
    def hibelow50(self):
        if self.num > self.maxnum//2:
            self.var = ('the number is greater than ' + str(self.maxnum//2) + '\npoints:' + str(self.points))
        elif self.num < 25:
            self.var = ('the number is ' + str(self.maxnum//2) + 'below\npoints: ' + str(self.points))

    def lowhigh(self):
        if self.ans > self.num:
            self.var = ('Incorrect Guess, Lower Please\npoints: ' + str(self.points))
            
        else:
            self.var = ('Incorrect Guess, Higher Please\npoints: ' + str(self.points))
    
    def oddeven(self):
        if self.num%2 == 0:
            self.var = ("Hint: it's an even number\npoints: " + str(self.points))
        else:
            self.var = ("Hint: it's an odd number\npoints: " + str(self.points))
        
    def minuspoints(self):
        self.points -= 10
        self.mylabel1.delete(1.0, END)
        self.mylabel1.insert(END, self.var)
        self.entry.delete(0, END)

    def reset(self):
        self.num = random.randint(1, self.maxnum)
        self.points = 100

    def answer(self):
        
        
        self.ans = int(self.entry.get())
        
        if self.ans == self.num:
                self.mylabel1.delete(1.0, END)
                self.var = ('Correct! the answer is '  + str(self.num) + 
                            '\npoints:' + str(self.points)
                            + '\nGame has been Reset')
                self.mylabel1.insert(END, self.var)
                self.entry.delete(0, END)
                self.reset()
        elif self.ans != self.num:
            if self.points == 100:
                self.points -= 10
            if self.points == 80:
                self.hibelow50()
                self.minuspoints()
            
            elif self.points == 50:
                self.oddeven()
                self.minuspoints()
            
            else:
                self.lowhigh()    
                self.minuspoints()
                if self.points == 0:
                    self.giveup()
    
    def click(self, number):
        self.number = number
        self.new = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, self.new + self.number)
    
    def giveup(self):
        self.mylabel1.delete(1.0, END)
        self.var = ('The correct Answer is ' + str(self.num) + '\nGame has been Reset')
        self.mylabel1.insert(END, self.var)
        self.entry.delete(0, END)
        self.reset()
    
    def __init__(self, master):
        self.num = random.randint(1,50)
        self.points = 100
        self.maxnum = 50
        self.var = ('Guess the number from 1 to ' + str(self.maxnum))
        self.mylabel1 = Text(root, height=4, width=30, bg='#373740', fg='#21c918')
        self.mylabel1.columnconfigure(0, weight=1)
        self.mylabel1.grid(row=0, column=0, columnspan=3)
        self.mylabel1.insert(END, self.var)
        self.mylabel1.configure(font=('Fixedsys', 10,))
        
        
        self.entry = Entry(root, borderwidth=5)
        self.entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=N+S+E+W)

        self.button1 = Button(root, text='1', width=8, bg='#293040', font=helv36, command=lambda: self.click("1"))
        self.button1.grid(row=2,column=0, padx=10, pady=5, sticky=N+S+E+W)

        self.button2 = Button(root, text='2', width=8, bg='#293040', font=helv36, command=lambda: self.click("2"))
        self.button2.grid(row=2,column=1, padx=10, pady=5, sticky=N+S+E+W)

        self.button3 = Button(root, text='3', width=8, bg='#293040', font=helv36, command=lambda: self.click("3"))
        self.button3.grid(row=2,column=2, padx=10, pady=5, sticky=N+S+E+W)


        self.button4 = Button(root, text='4', width=8, bg='#293040', font=helv36, command=lambda: self.click("4"))
        self.button4.grid(row=3,column=0, padx=10, pady=5, sticky=N+S+E+W)


        self.button5 = Button(root, text='5', width=8, bg='#293040', font=helv36, command=lambda: self.click("5"))
        self.button5.grid(row=3,column=1, padx=10, pady=5, sticky=N+S+E+W)

        self.button6 = Button(root, text='6', width=8, bg='#293040', font=helv36, command=lambda: self.click("6"))
        self.button6.grid(row=3,column=2, padx=10, pady=5, sticky=N+S+E+W)

        self.button7 = Button(root, text='7', width=8, bg='#293040', font=helv36, command=lambda: self.click("7"))
        self.button7.grid(row=4,column=0, padx=10, pady=5, sticky=N+S+E+W)

        self.button8 = Button(root, text='8', width=8, bg='#293040', font=helv36, command=lambda: self.click("8"))
        self.button8.grid(row=4,column=1, padx=10, pady=5, sticky=N+S+E+W)

        self.button9 = Button(root, text='9', width=8, bg='#293040', font=helv36, command=lambda: self.click("9"))
        self.button9.grid(row=4,column=2, padx=10, pady=5, sticky=N+S+E+W)

        self.button0 = Button(root, text='0', width=8, bg='#293040', font=helv36, command=lambda: self.click("0"))
        self.button0.grid(row=5,column=0, padx=10, pady=5, sticky=N+S+E+W)

        self.buttonenter = Button(root, text='Enter', width=8, bg='#293040', font=helv36, command=self.answer)
        self.buttonenter.grid(row=5,column=1, padx=10, pady=5, sticky=N+S+E+W)



        self.answerbutton = Button(root, text='Give Up', width=8, bg='#293040', font=helv36, command=self.giveup)
        self.answerbutton.grid(row=5,column=2, padx=10, pady=5, sticky=N+S+E+W)
    
        self.clearbutton = Button(root, text='Clear', bg='#293040', font=helv36, command=lambda: self.entry.delete(0, END))
        self.clearbutton.grid(row=6, column=0, columnspan=1, padx=10, pady=5, sticky=N+S+E+W) 

        self.level = Button(root, text='Difficulty', width=8, bg='#293040', font=helv36, command=self.level)    
        self.level.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky=N+S+E+W) 


e = GuessGame(root)
root.mainloop()
