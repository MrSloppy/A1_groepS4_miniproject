from tkinter import *
#from tkinter.ttk import *
from tkinter import ttk



Gfont=("helvetica", 40, "bold")
Buttonfont=("helvetica", 16)

def venster2(event):
    Button1.place(x=1000,y=1000)
    Button2.place(x=1000,y=1000)
    Button3.place(x=1000,y=1000)
    Button4.place(x=1000,y=1000)
    Button5.place(x=1000,y=1000)
    label1.pack_forget()
    label2.pack(side=BOTTOM)
    label3.place(x=2000,y=2000)
    Button6.place(x=200, y=300)
    Button7.place(x=400, y=300)
    Button8.place(x=650,y=470)

def venster3(event):
    master = Tk()
    master.resizable(width=0, height=0)
    master.geometry("800x600")
    master.config(bg="gold")

    label_huidig_station = Label(master, text = "Huidig station")
    label_huidig_station.place(x=100, y=100)
    label_Tijd0 = Label(master, text = "Tijd0")
    label_Tijd0.place(x = 200, y= 150 )
    label_Eindbestemming0 = Label(master, text = "Eindbestemming0")
    label_Eindbestemming0.place(x = 300, y = 150)
    label_Spoor0 = Label(master, text = "Spoor0")
    label_Spoor0.place(x = 550, y = 150)
    label_Typetrein0 = Label(master, text = "TypeTrein0")
    label_Typetrein0.place(x= 320, y = 200)

    label_Tijd1 = Label(master, text = "Tijd1")
    label_Tijd1.place(x = 200, y= 250 )
    label_Eindbestemming1 = Label(master, text = "Eindbestemming1")
    label_Eindbestemming1.place(x = 300, y = 250)
    label_Spoor1 = Label(master, text = "Spoor1")
    label_Spoor1.place(x = 550, y = 250)
    label_Typetrein1 = Label(master, text = "TypeTrein1")
    label_Typetrein1.place(x= 320, y = 300)

    label_Tijd2 = Label(master, text = "Tijd2")
    label_Tijd2.place(x = 200, y= 350 )
    label_Eindbestemming2 = Label(master, text = "Eindbestemming2")
    label_Eindbestemming2.place(x = 300, y = 350)
    label_Spoor2 = Label(master, text = "Spoor2")
    label_Spoor2.place(x = 550, y = 350)
    label_Typetrein2 = Label(master, text = "TypeTrein2")
    label_Typetrein2.place(x= 320, y = 400)

    label_Tijd3 = Label(master, text = "Tijd3")
    label_Tijd3.place(x = 200, y= 450 )
    label_Eindbestemming3 = Label(master, text = "Eindbestemming3")
    label_Eindbestemming3.place(x = 300, y = 450)
    label_Spoor3 = Label(master, text = "Spoor3")
    label_Spoor3.place(x = 550, y = 450)
    label_Typetrein3 = Label(master, text = "TypeTrein3")
    label_Typetrein3.place(x= 320, y = 500)

def venster4(event):
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000, y=1000)
    Button9.place(x=150,y=470)
    AnderStation.pack()

def venster5(event):
    Button9.place(x=1000,y=1000)
    AnderStation.pack_forget()

def reset(event):
    label1.pack()
    label3.pack()
    Button1.place(x=0,y=425)
    Button2.place(x=160,y=425)
    Button3.place(x=325,y=425)
    Button4.place(x=490,y=425)
    Button5.place(x=650, y=425)
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000,y=1000)
    Button9.place(x=1000,y=1000)
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
    global Button5
    global label2
    global label3
    global Button6
    global Button7
    global HuidigStation
    global Button8
    global AnderStation
    global Button9
    global gegevens

    root = Tk()
    root.resizable(width=0, height=0)
    root.geometry("800x600")
    root.config(bg="gold")

    label1 = Label(root, height=3, bg="gold", fg="darkblue", text="Welkom bij de NS", font=Gfont)
    label1.pack()

    HuidigStation = Label(root, height=3, bg="gold", fg="darkblue", text="info huidig Station", font=Gfont)
    HuidigStation.pack_forget()

    AnderStation = Label(root, height=3, bg="gold", fg="darkblue", text="Selecteer een ander station", font=Gfont)
    AnderStation.pack_forget()

    gegevens = Label(root, height=3, bg="gold", fg="darkblue", text="gegevens", font=Gfont)
    gegevens.pack_forget()

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

    Button5 = Button(root, wraplength=129,width = 12, text="Reis informatie", bg = "#00246B", fg ="white", font = Buttonfont)
    Button5.bind('<Button-1>', venster2)
    Button5.pack()
    Button5.place(x=650, y=425)
    #Dropdownmenu

    Button6 = Button(root, wraplength=125, justify=LEFT, text="Info huidig station",bg = "#00246B", fg = "white",font = Buttonfont, width=10)
    Button6.bind('<Button-1>', venster3)
    Button6.pack()
    Button6.place(x=1000,y=1000)

    Button7 = Button(root, wraplength=125, justify=LEFT, text="Info ander station",bg = "#00246B", fg = "white",font = Buttonfont, width=10)
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

    Button8 = Button(root, wraplength=125, justify=LEFT, text="Terug naar startscherm",bg = "#00246B", fg = "white",font = Buttonfont, width=10)
    Button8.bind('<Button-1>', reset)
    Button8.pack()
    Button8.place(x=1000,y=1000)

    Button9 = Button(root, wraplength=125, justify=LEFT, text="Gegevens",bg = "#00246B", fg = "white",font = Buttonfont, width=10)
    Button9.bind('<Button-1>', venster5)
    Button9.pack()
    Button9.place(x=1000,y=1000)


    root.mainloop()



venster1()