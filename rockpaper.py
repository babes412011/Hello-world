import tkinter as tk #not yet done
import random
from PIL import ImageTk, Image
import os

class RPSgame(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui_setting()
        self.widget()
        
        
    
    
    def gui_setting(self): 
        root.title('Rock, Paper, Scissor')
        root.geometry('800x520')
        root.config(bg = "#c1cbdb")
        root.grid_columnconfigure(1,weight=1)
        root.grid_rowconfigure(0,weight=1)   
        
        
        
    def widget(self):    
        frame1 = tk.Frame(root, bg='#6c7a70')
        frame1.pack(side='top')
            
        frame2 = tk.Frame(root, bg='#424f45')
        frame2.pack()
            
        frame3 = tk.Frame(root, bg='#6c7a70')
        frame3.pack()

        self.label1 = tk.Label(frame1, text='Rock, Paper, Scissor Game with\nToss coin as Tie Breaker',bg='#6c7a70')
        self.label1.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='n,s,w,e')

        self.label2 = tk.Label(frame2, height=25, width=45, text='player')
        self.label2.grid(row=0, column=0, sticky='n,s,w,e')

        self.label3 = tk.Label(frame2, text='VS', width=7, bg='#242526')
        self.label3.grid(row=0, column=1, sticky='n,s,w,e')

        self.label4 = tk.Label(frame2, height=25, width=45, text='pc')
        self.label4.grid(row=0, column=2, sticky='n,s,w,e')

        self.rock = tk.Button(frame3, text='ROCK', padx=20, width=10,pady=10, command=lambda: self.player_choice('rock'))
        self.rock.grid(row=0, column=0, padx=5, pady=5, sticky='n,s,w,e')

        self.paper = tk.Button(frame3, text='PAPER', padx=20, width=10, pady=10, command=lambda: self.player_choice('paper'))
        self.paper.grid(row=0, column=1, padx=5, pady=5, sticky='n,s,w,e')

        self.scissors = tk.Button(frame3, text='SCISSORS', width=10, padx=20, pady=10, command=lambda: self.player_choice('scissors'))
        self.scissors.grid(row=0, column=2, padx=5, pady=5, sticky='n,s,w,e')

    def player_choice(self, choice):
        self.choice = choice
        self.weopon_choice()
        self.label2.configure(image=self.imgs, width=250, height=325)
        self.pc_choice()
    
    def weopon_choice(self):
        self.player_image = os.listdir('C:\\Users\\Photoshop\\Desktop\\VScode\\rockpaperscissors\\' + self.choice)
        num = random.randint(0,(len(self.player_image)-1))
        imgp = Image.open('C:/Users\Photoshop/Desktop/VScode/rockpaperscissors/'+ self.choice + '/' + self.player_image[num])
        imgp = imgp.resize((200,200), Image.ANTIALIAS)
        self.imgs = ImageTk.PhotoImage(imgp)

    def pc_choice(self):
        self.choicelist = ['rock','paper','scissors']
        self.pcnum = random.randint(0,2)
        self.pcchoice = self.choicelist[self.pcnum]
        self.pcimage = os.listdir('C:\\Users\\Photoshop\\Desktop\\VScode\\rockpaperscissors\\pc')
        imgpc = Image.open('C:/Users\Photoshop/Desktop/VScode/rockpaperscissors/pc/' + self.pcchoice + '.jpg')
        imgpc = imgpc.resize((200,200), Image.ANTIALIAS)
        self.pcimg = ImageTk.PhotoImage(imgpc)
        self.label4.configure(image=self.pcimg, width=250, height=325)

    


if __name__ == '__main__':
   root = tk.Tk()
   main_app =  RPSgame(root)
   root.mainloop()
