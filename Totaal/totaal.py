from tkinter import *



Gfont=("arial", 45, "bold")
Buttonfont=("arial", 16)

def venster2(event):
    Button1.place(x=1000,y=1000)
    Button2.place(x=1000,y=1000)
    Button3.place(x=1000,y=1000)
    Button4.place(x=1000,y=1000)
    label1.pack_forget()
    label2.place(x=2000,y=2000)
    Button6.place(x=200, y=300)
    Button7.place(x=400, y=300)
    Button8.place(x=650,y=530)

def venster3(event):
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000, y=1000)
    HuidigStation.pack()

def venster4(event):
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000, y=1000)
    AnderStation.pack()

def reset(event):
    label1.pack()
    Button1.place(x=50,y=425)
    Button2.place(x=225,y=425)
    Button3.place(x=425,y=425)
    Button4.place(x=600,y=425)
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000,y=1000)
    label2.pack(side=BOTTOM)
    Button8.place(x=1000,y=1000)
    HuidigStation.pack_forget()
    AnderStation.pack_forget()

def venster1():
    global label1
    global root
    global Button1
    global Button2
    global Button3
    global Button4
    global label2
    global Button6
    global Button7
    global HuidigStation
    global Button8
    global AnderStation

    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry("800x600")
    root.config(bg="gold")

    label1 = Label(root, height=3, bg="gold", fg="darkblue", text="Welkom bij de NS", font=Gfont)
    label1.pack()

    HuidigStation = Label(root, height=3, bg="gold", fg="darkblue", text="Huidig Station", font=Gfont)
    HuidigStation.pack_forget()

    AnderStation = Label(root, height=3, bg="gold", fg="darkblue", text="Selecteer een ander station", font=Gfont)
    AnderStation.pack_forget()

    Button1 = Button(root, wraplength=129, width = 12, text="Ik wil naar Amsterdam", bg = "#00246B", fg ="white", font = Buttonfont)
    Button1.pack()
    Button1.place(x=0, y=425)

    Button2 = Button(root,wraplength=129, width = 12, text="Kopen los kaartje", bg = "#00246B", fg ="white", font = Buttonfont)
    Button2.pack()
    Button2.place(x=160, y=425)

    Button3 = Button(root, wraplength=129,width = 12, text="Kopen OV-chipkaart", bg = "#00246B", fg ="white", font = Buttonfont) # hier moet een command
    Button3.pack()
    Button3.place(x=325, y=425)

    Button4 = Button(root, wraplength=129,width = 12, text="Ik wil naar het buitenland", bg = "#00246B", fg ="white", font = Buttonfont)
    Button4.pack()
    Button4.place(x=490, y=425)

    Button5 = Button(root, wraplength=129,width = 12, text="Reis informatie", bg = "red", fg ="white", font = Buttonfont)
    Button5.bind('<Button-1>', venster2)
    Button5.pack()
    Button5.place(x=650, y=425)
    #Dropdownmenu

    Button6 = Button(root, wraplength=125, justify=LEFT, text="Info voor huidig station",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button6.bind('<Button-1>', venster3)
    Button6.pack()
    Button6.place(x=1000,y=1000)

    Button7 = Button(root, wraplength=125, justify=LEFT, text="Info voor ander station",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button7.bind('<Button-1>', venster4)
    Button7.pack()
    Button7.place(x=1000,y=1000)

    photo1 = PhotoImage(file="Welkomsttekst.png") # je geeft een PhotoImage file een variabele
    photo5 = PhotoImage(file="Bar.png")

    photo5=PhotoImage(file="Bar.png")
    label2 = Label(root, image=photo5, bg="darkblue")
    label2.pack(side=BOTTOM)

    label3 = Label(root, image=photo1, bg="#FFCC00") #je zet een foto in de label waarvan je eerder de naam had gegeven
    label3.pack(side=TOP)

    Button8 = Button(root, wraplength=125, justify=LEFT, text="Terug naar startscherm",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button8.bind('<Button-1>', reset)
    Button8.pack()
    Button8.place(x=1000,y=1000)

    root.mainloop()

venster1()