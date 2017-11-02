import time
import tkinter as tk
from tkinter import ttk, N, S, E, W, Button, Frame, Tk, OptionMenu, Label, Text
from tkinter import StringVar, BooleanVar
# https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master = master

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

def helloworld():
    root = Tk()
    app = Application(master=root)
    app.mainloop()

# https://pythonspot.com/en/tk-dropdown-example/
def drop_down():
    ''''''
    root = Tk()
    root.title("Tk dropdown example")

    # Add a grid
    mainframe = Frame(root)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)

    # Create a Tkinter variable
    tkvar = StringVar(root)

    # Dictionary with options
    choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
    tkvar.set('Pizza') # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)

    # on change dropdown value
    def change_dropdown(*args):
        print( tkvar.get() )

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    root.mainloop()

def show_grid():
    '''http://www.tkdocs.com/tutorial/grid.html'''
    root = Tk()

    content = ttk.Frame(root, padding=(3,3,12,12))
    frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
    namelbl = ttk.Label(content, text="Name")
    name = ttk.Entry(content)

    onevar = BooleanVar()
    twovar = BooleanVar()
    threevar = BooleanVar()

    onevar.set(True)
    twovar.set(False)
    threevar.set(True)

    one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
    two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
    three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
    ok = ttk.Button(content, text="Okay")
    cancel = ttk.Button(content, text="Cancel")

    content.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
    namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
    name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
    one.grid(column=0, row=3)
    two.grid(column=1, row=3)
    three.grid(column=2, row=3)
    ok.grid(column=3, row=3)
    cancel.grid(column=4, row=3)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.columnconfigure(1, weight=3)
    content.columnconfigure(2, weight=3)
    content.columnconfigure(3, weight=1)
    content.columnconfigure(4, weight=1)
    content.rowconfigure(1, weight=1)

    root.mainloop()

def logging_window():
    
    root = Tk()
    log = Text(root, state='disabled', width=80, height=24, wrap='none')
    log.grid()
    
    def writeToLog(msg):
        numlines = log.index('end - 1 line').split('.')[0]
        log['state'] = 'normal'
        if numlines==24:
            log.delete(1.0, 2.0)
        if log.index('end-1c')!='1.0':
            log.insert('end', '\n')
        log.insert('end', msg)
        log['state'] = 'disabled'
        
    writeToLog("hello world")    
    root.mainloop()
    print("got here")
    while True:
        time.sleep(1)
        writeToLog("hello Again, nn...")
if __name__ == '__main__':
#     helloworld()
#     drop_down()
    show_grid()
#     logging_window()

        
    

