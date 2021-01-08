import tkinter as tk #optional tosscoin
import random
from PIL import ImageTk, Image
import os

class RPSgame(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.mypoints = 0
        self.pcpoints = 0
        self.gui_setting()
        self.on_off = 'ON'
        self.widget()
        self.rock['state'] = tk.DISABLED
        self.paper['state'] = tk.DISABLED
        self.scissors['state'] = tk.DISABLED
        
    
    
    def gui_setting(self): 
        root.title('Rock, Paper, Scissor')
        root.geometry('800x570')
        root.config(bg = "#c1cbdb")
        root.grid_columnconfigure(1,weight=1)
        root.grid_rowconfigure(0,weight=1)   
        
        
        
    def widget(self):
         
        frame1 = tk.Frame(root, bg='#6c7a70')
        frame1.pack(side='top')
            
        frame2 = tk.Frame(root, bg='#222326')
        frame2.pack()
            
        frame3 = tk.Frame(root, bg='#6c7a70')
        frame3.pack()

        self.label1 = tk.Label(frame1, text='Rock, Paper, Scissor Game with\nToss coin as Tie Breaker',bg='#6c7a70')
        self.label1.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='n,s,w,e')

        self.points = tk.Text(frame1,height=3, width=10)
        self.points.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='n,s,w,e')
        self.points.insert('end', 'Player:' + str(self.mypoints) + '\nPc:' + str(self.pcpoints))

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

        self.gamemode = tk.Button(frame3, text='Game Mode', width=10, padx=20, pady=10,command=self.mode)
        self.gamemode.grid(row=1, column=1, padx=5, pady=5, sticky='n,s,w,e')
        
        self.gamereset = tk.Button(frame3, text="Reset", width=10, padx=20, pady=10, command=self.greset)
        self.gamereset.grid(row=1,column=0, padx=5, pady=5, sticky='n,s,w,e')

        self.tossoff = tk.Button(frame3, text='TossCoin On/Off', width=10, padx=20, pady=10,command=self.toss_button)
        self.tossoff.grid(row=1, column=2,padx=5, pady=5, sticky='n,s,w,e')
        
        self.toss_text = tk.Text(frame3, width=20, height=1)
        self.toss_text.grid(row=2,column=0, columnspan=3,sticky='n,s,w,e')
        self.toss_text.tag_configure("center", justify='center')
        self.toss_text.insert('1.0', 'Tosscoin')
        self.toss_text.tag_add("center", "1.0", "end")
    
    def toss_button(self):
        
        if self.on_off == 'OFF':
            self.on_off = 'ON'
            self.toss_text.delete('1.0', 'end')
            self.toss_text.insert('1.0', 'Toss Coin Turned On')
            self.toss_text.tag_add("center", "1.0", "end")
        elif self.on_off == 'ON':
            self.on_off = 'OFF'
            self.toss_text.delete('1.0', 'end')
            self.toss_text.insert('1.0', 'Toss Coin Turned Off')
            self.toss_text.tag_add("center", "1.0", "end")   
    
    def player_choice(self, choice):
        self.choice = choice
        self.weopon_choice()
        self.label2.configure(image=self.imgs, width=250, height=325)
        self.pc_choice()
        self.compare()
        if self.mypoints == self.bpoints or self.pcpoints == self.bpoints:
            self.points.delete(1.0, 'end')
            self.points.insert('end', 'Player:' + str(self.mypoints) + '\nPc:' + str(self.pcpoints) + '\nEnd Game')
            self.reset()
            
    def weopon_choice(self):
        self.player_image = os.listdir('C:\\Users\\Photoshop\\Desktop\\VScode\\rockpaperscissors\\' + self.choice)
        num = random.randint(0,(len(self.player_image)-1))
        imgp = Image.open(r'C:/Users\Photoshop/Desktop/VScode/rockpaperscissors/'+ self.choice + '/' + self.player_image[num])
        imgp = imgp.resize((200,200), Image.ANTIALIAS)
        self.imgs = ImageTk.PhotoImage(imgp)

    def pc_choice(self):
        self.choicelist = ['rock','paper','scissors']
        self.pcnum = random.randint(0,2)
        self.pcchoice = self.choicelist[self.pcnum]
        self.pcimage = os.listdir('C:\\Users\\Photoshop\\Desktop\\VScode\\rockpaperscissors\\pc')
        imgpc = Image.open(r'C:/Users\Photoshop/Desktop/VScode/rockpaperscissors/pc/' + self.pcchoice + '.jpg')
        imgpc = imgpc.resize((200,200), Image.ANTIALIAS)
        self.pcimg = ImageTk.PhotoImage(imgpc)
        self.label4.configure(image=self.pcimg, width=250, height=325)

    def addpoints(self):
        self.points.delete(1.0, 'end')
        self.points.insert('end', 'Player:' + str(self.mypoints) + '\nPc:' + str(self.pcpoints) + '\nHappy Gaming')
    
    def draw(self):
        self.top = tk.Toplevel(self.master)
        self.top.title("Draw")
        self.top.geometry('300x220')
        self.coinlabel = tk.Label(self.top)
        self.coinlabel.pack()
        coinimg = Image.open(r'C:/Users\Photoshop/Desktop/VScode/rockpaperscissors/coins/coin.jpg')
        coinimg = coinimg.resize((100,100), Image.ANTIALIAS)
        self.postimg = ImageTk.PhotoImage(coinimg)
        self.coinlabel.configure(image=self.postimg, width=200, height=100)
        self.exittop = tk.Button(self.top,text='Exit',command=self.top.destroy)
        self.exittop.pack(side='bottom')
        self.heads = tk.Button(self.top, text='Heads', padx=6,pady=10,command=lambda:self.tosscoin('heads'))
        self.heads.pack(side='bottom')
        self.tails = tk.Button(self.top, text='Tails', padx=6,pady=10,command=lambda:self.tosscoin('tails'))
        self.tails.pack(side='bottom')
        self.coin = random.randint(0,1)
        self.toplabel = tk.Label(self.top, text='Head or Tails')
        self.toplabel.pack(side='top')
    
    
    
    def tosscoin(self,picked):
        self.ans = picked
        if self.coin == 0:
            self.coin = 'heads'
        elif self.coin == 1:
            self.coin = 'tails'
        if self.ans == self.coin:
            self.toplabel.configure(text='Correct, 1 point for you')
            self.mypoints += 1
            self.addpoints()
        elif self.ans != self.coin:
            self.toplabel.configure(text='Sorry, The Answer is ' + self.coin + ' 1 point for PC')
            self.pcpoints += 1
            self.addpoints()
        if self.mypoints == self.bpoints or self.pcpoints == self.bpoints:
            self.points.delete(1.0, 'end')
            self.points.insert('end', 'Player:' + str(self.mypoints) + '\nPc:' + str(self.pcpoints) + '\nEnd Game')
            self.reset()
        self.heads['state'] = tk.DISABLED
        self.tails['state'] = tk.DISABLED
    
    
    def reset(self):
        self.mypoints = 0
        self.pcpoints = 0
        self.rock['state'] = tk.DISABLED
        self.paper['state'] = tk.DISABLED
        self.scissors['state'] = tk.DISABLED
        self.gamemode['state'] = tk.DISABLED
        
    
    def greset(self):
        self.reset()
        self.addpoints()
        self.gamemode['state'] = tk.NORMAL
    
    def mode(self):
        self.topmode = tk.Toplevel(self.master)
        self.topmode.title("Choose a Mode")
        self.topmode.geometry('300x220')
        self.mbutton1 = tk.Button(self.topmode, text='Best of 3',padx=6,pady=6,command=lambda:self.best(3))
        self.mbutton1.pack()
        self.mbutton2 = tk.Button(self.topmode, text='Best of 5',padx=6,pady=6,command=lambda:self.best(5))
        self.mbutton2.pack()

    def best(self,bestnum):
        self.bpoints = bestnum
        self.rock['state'] = tk.NORMAL
        self.paper['state'] = tk.NORMAL
        self.scissors['state'] = tk.NORMAL
        self.topmode.destroy()
    
    def compare(self):
        if self.on_off == 'ON':
            if self.choice == self.pcchoice:
                self.draw()
        
            
        if self.choice == 'rock':
            if self.pcchoice == 'scissors':
                self.mypoints += 1
                self.addpoints()
            elif self.pcchoice == 'paper':
                self.pcpoints += 1
                self.addpoints()
        elif self.choice == 'paper':
            if self.pcchoice == 'rock':
                self.mypoints += 1
                self.addpoints()
            elif self.pcchoice == 'scissors':
                self.pcpoints += 1
                self.addpoints()
        elif self.choice == 'scissors':
            if self.pcchoice == 'paper':
                self.mypoints += 1
                self.addpoints()
            elif self.pcchoice == 'rock':
                self.pcpoints += 1
                self.addpoints()
        


if __name__ == '__main__':
    root = tk.Tk()
    main_app =  RPSgame(root)
    root.mainloop()
