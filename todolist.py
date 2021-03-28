import tkinter as tk
import datetime
from tkinter import messagebox
from tododb import todo_database
db = todo_database('todo.db')

class todo_list(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui_setting()
        self.widget()
        

    def gui_setting(self):
        root.title("To do Lists")
        root.geometry('500x450')

    def widget(self):
        
        
        
        self.text_field = tk.Text(root, height=10, width=25)
        self.text_field.pack()

        self.add_btn = tk.Button(root, text='Add to List', command=self.add)
        self.add_btn.pack()

        self.view_btn = tk.Button(root, text='View LIst', command=self.view)
        self.view_btn.pack()

        self.clear_btn= tk.Button(root, text='Remove',command=self.remove)
        self.clear_btn.pack()
    
        self.framelb = tk.Frame(root)
        self.framelb.pack()
        
        
        self.todolistbox = tk.Listbox(self.framelb, height=10, width=70)
        self.todolistbox.pack(side='left')

        self.scroll = tk.Scrollbar(self.framelb,)
        self.scroll.pack(side='left', fill='y')

        self.todolistbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.todolistbox.yview)
    
        self.todolistbox.bind('<<ListboxSelect>>', self.selected_item)
    
    
    
    def add(self):
        x = datetime.datetime.now()
        self.datenow = x.strftime('%b-%d-%Y')
        db.insert(self.text_field.get(1.0, 'end-1c'),('Date Posted ' + self.datenow))
        self.view()
        self.text_field.delete(1.0,'end')
    
    def view(self):
        self.todolistbox.delete(0,'end')
        for row in db.fetch():
            self.todolistbox.insert('end', row)
            
    def selected_item(self, event):
        index = self.todolistbox.curselection()[0]
        self.selected_item = self.todolistbox.get(index)

    

    
    
    def remove(self):
        db.remove(self.selected_item[0])
        self.view()
        








if __name__ == '__main__':
    root = tk.Tk()
    main_app = todo_list(root)
    root.mainloop()
