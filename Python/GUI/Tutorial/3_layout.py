"""
Exempelprogram för hur man kan bygga en bra layout för sin app.

"""

from tkinter import Tk, Frame, Menu
from tkinter import TOP, RIGHT,LEFT, X, Y, BOTH

# Frame https://www.tutorialspoint.com/python/tk_frame.htm
# pack() https://www.tutorialspoint.com/python/tk_pack.htm
# Menu https://www.tutorialspoint.com/python/tk_menu.htm



# Init
root = Tk()
root.title("Layout Example")
root.geometry('800x640')

# Layout
header = Frame(root, height=100, bg='red')
header.pack(side=TOP, fill=X)
appcontent = Frame(root, bg='blue')
appcontent.pack(fill=BOTH, expand=1)



# Extended Layout

right = Frame(appcontent, bg='green')
right.pack(side=RIGHT, fill=BOTH, expand=1)

middle = Frame(appcontent, bg='yellow')
middle.pack(side=RIGHT, fill=BOTH, expand=1)

left = Frame(appcontent, bg='purple')
left.pack(side=RIGHT, fill=BOTH, expand=1)
















def void():
    print("pressed something")

menubar = Menu(root)


#Skapar första meny-lista
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=void)
filemenu.add_command(label="Open", command=void)
filemenu.add_command(label="Save", command=void)
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
root.config(menu=menubar)


root.mainloop()
