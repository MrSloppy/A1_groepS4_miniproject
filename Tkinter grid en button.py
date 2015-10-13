__author__ = 'Koshin'
from tkinter import *



root = Tk()

Topframe = Frame(root)
Topframe.pack()#PACK PLAATST HET IN HET MIDDEN VAN DE WINDOW
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM) #JE HOEFT ALLEEN MAAR BOTTOM AAN TE GEVEN ALS JE OOK EEN TOP WILT

button1 = Button(Topframe, text = "button 1", fg="red")
button2 = Button(Topframe, text = "button 2", fg="blue")
button3 = Button(Topframe, text = "button 3", fg="purple")
button4 = Button(Topframe, text = "button 4", fg="brown")
#FG = FOREGROUND
#BG=BACKGGROUND

button1.pack(side = LEFT)
button2.pack(side = RIGHT)
button3.pack(side = TOP)
button4.pack(side = BOTTOM)

root.mainloop()#houdt de window in een loop vast zodat het niet weggaat
