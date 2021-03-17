import tkinter as tk
import random
from adjecdb import adj_database
db = adj_database('adj.db')

class adjectiv(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui_setting()
        self.widget()
        
        self.adjlist = ['Acidic:',
 'Bitter:',
 'Bittersweet:',
 'Briny:',
 'Citrusy:',
 'Cooling:',
 'Earthy:',
 'Fiery:',
 'Fresh:',
 'Fruity:',
 'Full-bodied:',
 'Herbal:',
 'Honeyed:',
 'Nutty:',
 'Rich:',
 'Robust:',
 'Sharp:',
 'Smoky:',
 'Sour:',
 'Spicy:',
 'Sweet:',
 'Tangy:',
 'Tart:',
 'Yeasty:',
 'Woody:',
 'Zesty:','Airy:',
 'Buttery:',
 'Chewy:',
 'Creamy:',
 'Crispy:',
 'Crumbly:',
 'Crunchy:',
 'Crusty:',
 'Delicate:',
 'Doughy:',
 'Fizzy:',
 'Flaky:',
 'Fluffy:',
 'Gooey:',
 'Hearty:',
 'Juicy:',
 'Silky:',
 'Sticky:',
 'Smooth:',
 'Succulent:',
 'Tender:',
 'Velvety:','Baked:',
 'Blanched:',
 'Blackened:',
 'Braised:',
 'Breaded:',
 'Broiled:',
 'Caramelized:',
 'Charred:',
 'Fermented:',
 'Fried:',
 'Glazed:',
 'Infused:',
 'Marinated:',
 'Poached:',
 'Roasted:',
 'Sauteed:',
 'Seared:',
 'Smoked:',
 'Whipped:']

    def gui_setting(self): 
        root.title('Food adjective generator')
        root.geometry('500x500')

    
    
    def widget(self):
        self.text_field = tk.Text(root, height=4, width=30)
        self.text_field.pack()
    
        self.gen_btn = tk.Button(root, text="Generate", command=self.gen_adj)
        self.gen_btn.pack()

        self.addlist_btn = tk.Button(root, text="Use Adjective", command=self.add_adj)
        self.addlist_btn.pack()

        self.view_usedadj_btn = tk.Button(root, text='View Used Adjectives', command=self.view_usedadj)
        self.view_usedadj_btn.pack()

        self.clear_btn = tk.Button(root, text='Clear List', command=self.clear_list)
        self.clear_btn.pack()
        

    def gen_adj(self):
        x = random.randint(0, len(self.adjlist)-1)
        self.new_adj = self.adjlist[x]
        self.text_field.delete(1.0,'end')
        self.text_field.insert('end', self.new_adj)
        

    def view_usedadj(self):
        self.text_field.delete(1.0,'end')
        for row in db.get_data():
            self.text_field.insert('end', row)

    def add_adj(self):
        db.addtodb(self.text_field.get(1.0,'end-1c'))

    def clear_list(self):
        db.delete_list()
        self.text_field.delete(1.0,'end')








if __name__ == '__main__':
    root = tk.Tk()
    main_app = adjectiv(root)
    root.mainloop()