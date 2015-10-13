from tkinter import * #tkinter GUI importen

TITLE_FONT = ("Times", 40, "bold")

root = Tk() #tkinter scherm aanmaken
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(800, 600))

topFrame = Frame(root.configure(background="#FFCC00"))
topFrame.pack(side=TOP)

bottomFrame = Frame(root) # een rechthoekig frame aanbrengen waar je widgets kan toevoegen/ je kan zelf de x en y bepalen
bottomFrame.pack(side=BOTTOM) # een frame aan de onderkant van het tkinter aanbrengen, hierdoor heb je dus ook gelijk een topframe

label1 = Label(root,height=3, font=TITLE_FONT,  text="Welkom bij NS", bg="#FFCC00", fg="#000066")
label1.pack(fill=X)
label2 = Label(root, text = "Preparing to do nothing", bg="#000066",  bd = 1, relief = SUNKEN, anchor = W)
label2.pack(side = BOTTOM, fill = X)



root.mainloop() #een mainloop aan het scherm toevoegen zodat het scherm blijft runnen

