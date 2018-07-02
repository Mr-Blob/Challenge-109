import tkinter as tk
import os.path
class FirstFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.pack()
        master.title("Main Application")
        master.geometry("600x400")

        self.button1 = tk.Button(self, text='1: Create/Edit New File', command=self.f1)
        self.button1.pack()
        self.button2 = tk.Button(self, text='2: Display File', command=self.f2)
        self.button2.pack()
        self.button3 = tk.Button(self, text='3', command=self.f3)
        self.button3.pack()

    def f1(self, event=None):
        self.destroy()
        self.app = CreateFrame(self.master)
    def f2(self, event=None):
        self.destroy()
        self.app = Frame2(self.master)
    def f3(self, event=None):
        self.destroy()
        self.app = Frame3(self.master)

        

class CreateFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.pack()
        master.title('Create New File')
        master.geometry('600x400')
        self.name = tk.Entry(self.master)
        self.name.pack()
        self.next = tk.Button(self, text='Next', command=self.nextframe)
        self.next.pack()
    def nextframe(self):
        self.filename = self.name.get()
        self.name.destroy()
        self.next.destroy()

                
        self.savework = tk.Button(self, text="Save", command= self.save)

        self.textty1 = tk.Text(self, height = 100, width = 100)
        
        self.textty1.focus()
        self.textbar = tk.Scrollbar(self)

        
        self.textbar.config(command=self.textty1.yview)
        self.textty1.config(yscrollcommand=self.textbar.set)
        self.savework.pack()
        self.textty1.pack(side=tk.LEFT, fill=tk.Y)
        self.textbar.pack(side=tk.RIGHT, fill=tk.Y)

        if os.path.isfile('{}.txt'.format(self.filename)) == True:
            with open('{}.txt'.format(self.filename), 'r') as f:
                data = f.read()
                self.textty1.insert(tk.END, data)
                self.textty1.pack(side=tk.LEFT, fill=tk.Y)
        else:
            with open('{}.txt'.format(self.filename), 'r') as f:
                f.close()
    def save(self):
        with open('{}.txt'.format(self.filename), 'w') as f:
            text = self.textty1.get(tk.END)
            f.write(text)



    def save(self):
        text = self.textty1.get("1.0", 'end-1c')
        with open('{}.txt'.format(self.filename), 'w') as f:
            f.write(text)
        self.destroy()
        self.app = FirstFrame(self.master)
        


class Frame2(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.pack()
        master.title('Display File')
        master.geometry('600x400')
        self.name = tk.Entry(self.master)
        self.name.pack()
        self.next = tk.Button(self, text='Next', command=self.nextframe)
        self.next.pack()
    def nextframe(self):
        self.filename = self.name.get()
        self.next.destroy()
        self.name.destroy()
        self.backbutton = tk.Button(self, text='Back', command=self.goback)
        self.backbutton.pack()
        self.textbox = tk.Text(self, height = 100, width = 100)
        self.textbox.pack()
        with open('{}.txt'.format(self.filename), 'r') as f:
            self.textbox.configure(state='normal')
            self.textbox.insert(tk.END, f.read())
            self.textbox.configure(state='disabled')
            
    def goback(self):
        self.destroy()
        self.app = FirstFrame(self.master)


class Frame3(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.pack()
        master.title('Add New Item to File')
        master.geometry('600x400')



if __name__=="__main__":
    root = tk.Tk()
    app=FirstFrame(root)
    root.mainloop()