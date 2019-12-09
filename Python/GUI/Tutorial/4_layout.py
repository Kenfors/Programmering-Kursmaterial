"""
Exempelprogram för hur man kan bygga en bra layout för sin app.

"""

from tkinter import Tk, Frame, Menu
from tkinter import TOP, RIGHT,LEFT, X, Y, BOTH

# Frame https://www.tutorialspoint.com/python/tk_frame.htm
# pack() https://www.tutorialspoint.com/python/tk_pack.htm
# Menu https://www.tutorialspoint.com/python/tk_menu.htm


# Klassen LayoutApplication
# 
# 
class LayoutApplication(Tk):
    header : Frame
    left : Frame
    right : Frame
    center : Frame

    def __init__(self):
        super().__init__()
        super().title("Layout Example")
        super().geometry('800x640')

        self.buildMenu()
        self.buildLayout()


    
    def buildLayout(self):
        # Layout
        header = Frame(self, height=100, bg='red')
        header.pack(side=TOP, fill=X)

        appcontent = Frame(self, bg='blue')
        appcontent.pack(fill=BOTH, expand=1)
        
        self.right = Frame(appcontent, bg='green')
        self.right.pack(side=RIGHT, fill=BOTH, expand=1)

        self.center = Frame(appcontent, bg='yellow')
        self.center.pack(side=RIGHT, fill=BOTH, expand=1)

        self.left = Frame(appcontent, bg='purple')
        self.left.pack(side=RIGHT, fill=BOTH, expand=1)
    
    def void(self):
        print("pressed something")

    def buildMenu(self):
        menubar = Menu(self)


        #Skapar första meny-lista
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.void)
        filemenu.add_command(label="Open", command=self.void)
        filemenu.add_command(label="Save", command=self.void)
        menubar.add_cascade(label="File", menu=filemenu)


        #Skapar nästa meny-lista
        othermenu = Menu(menubar, tearoff=0)
        othermenu.add_checkbutton(label="Check Me !")
        menubar.add_cascade(label="Other", menu=othermenu)


        #Skapar hierarkisk meny-lista
        doublemenu = Menu(menubar, tearoff=0)
        doublemenu.add_command(label="button")
        innermenu = Menu(doublemenu, tearoff=0)
        innermenu.add_command(label="one")
        innermenu.add_command(label="two")
        innermenu.add_command(label="ten")
        doublemenu.add_cascade(label="innerMenu", menu=innermenu)
        menubar.add_cascade(label="Double", menu=doublemenu)

        #Lägger till menyn
        self.config(menu=menubar)

# Init
App = LayoutApplication()
App.mainloop()
