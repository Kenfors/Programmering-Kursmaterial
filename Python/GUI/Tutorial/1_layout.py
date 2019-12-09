"""
Exempelprogram för hur man kan bygga en bra layout för sin app.

"""

from tkinter import Tk, Frame
from tkinter import TOP, X, BOTH




# Starta ett nytt window. Kalla den för "root", det är första noden som kommer innehålla alla andra noder.
# definera titeln
# definera window-storleken X * Y
root = Tk()
root.title("Layout Example")
root.geometry('800x640')



# Frame https://www.tutorialspoint.com/python/tk_frame.htm
# pack() https://www.tutorialspoint.com/python/tk_pack.htm
#
# Frame har samma funktion som "div" inom webutveckling. Det är en ram, som inte har en speciell funktion
# utan syften är att gruppera flera widgets. root är också en frame.
# 
# Vi skapar en Frame som vi ska ha längst upp i appen, som kan innehålla saker senare.
# Vi vill att den alltid ska ha samma proportioner, hela X-led men bara 100 y-led och längst upp.
# Bakgrundsfärgen röd så vi ska se vart den är.
header = Frame(root, height=100, bg='red')
header.pack(side=TOP, fill=X)

# En frame för allt content. Blå för att känna igen den.
# fill + expand => fyll ut och expandera.
appcontent = Frame(root, bg='blue')
appcontent.pack(fill=BOTH, expand=1)





root.mainloop()
