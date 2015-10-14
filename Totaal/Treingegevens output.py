__author__ = 'Koshin'
from tkinter import *
from tkinter import ttk

Gfont=("helvetica", 40, "bold")
Buttonfont=("helvetica", 16)


def Frame1():
    master = Tk()
    master.resizable(width=0, height=0)
    master.geometry("800x600")
    master.config(bg="gold")

    label_huidig_station = Label(master, text = "{}".format(bestemming_input))
    label_huidig_station.place(x=100, y=100)
    label_Tijd0 = Label(master, text = "{}").format(vertrektijd_list[0]))
    label_Tijd0.place(x = 200, y= 150 )
    label_Eindbestemming0 = Label(master, text = "{}".format(eindbestemming_list[0]))
    label_Eindbestemming0.place(x = 300, y = 150)
    label_Spoor0 = Label(master, text = "{}".format(spoor_list[0]))
    label_Spoor0.place(x = 550, y = 150)
    label_Typetrein0 = Label(master, text = "{}".format(treinsoort_list[0]))
    label_Typetrein0.place(x= 320, y = 200)

    label_Tijd1 = Label(master, text = "{}".format(vertrektijd_list[1]))
    label_Tijd1.place(x = 200, y= 250 )
    label_Eindbestemming1 = Label(master, text = "{}".format(eindbestemming_list[1]))
    label_Eindbestemming1.place(x = 300, y = 250)
    label_Spoor1 = Label(master, text = "{}".format(spoor_list[1]))
    label_Spoor1.place(x = 550, y = 250)
    label_Typetrein1 = Label(master, text = "{}".format(treinsoort_list[1]))
    label_Typetrein1.place(x= 320, y = 300)

    label_Tijd2 = Label(master, text = "{}".format(vertrektijd_list[2]))
    label_Tijd2.place(x = 200, y= 350 )
    label_Eindbestemming2 = Label(master, text = "{}".format(eindbestemming_list[2]))
    label_Eindbestemming2.place(x = 300, y = 350)
    label_Spoor2 = Label(master, text = "{}".format(spoor_list[2]))
    label_Spoor2.place(x = 550, y = 350)
    label_Typetrein2 = Label(master, text = "{}".format(treinsoort_list[2]))
    label_Typetrein2.place(x= 320, y = 400)

    label_Tijd3 = Label(master, text = "{}".format(vertrektijd_list[3]))
    label_Tijd3.place(x = 200, y= 450 )
    label_Eindbestemming3 = Label(master, text = "{}".format(eindbestemming_list[3]))
    label_Eindbestemming3.place(x = 300, y = 450)
    label_Spoor3 = Label(master, text = "{}".format(spoor_list[3]))
    label_Spoor3.place(x = 550, y = 450)
    label_Typetrein3 = Label(master, text = "{}".format(treinsoort_list[3]))
    label_Typetrein3.place(x= 320, y = 500)

    master.mainloop()
Frame1()