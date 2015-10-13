from tkinter import * #tkinter GUI importen

root = Tk() #tkinter scherm aanmaken



TITLE_FONT = ("helvetica", 40, "bold") #



#een foto toevoegen aan dit bestand
photo1 = PhotoImage(file="Welkomsttekst.png") # je geeft een PhotoImage file een variabele
photo5 = PhotoImage(file="Bar.png")



root.resizable(width=FALSE, height=FALSE) #je geeft aaan dat je de root(Tk) niet kan veranderen qua grootte
root.geometry('{}x{}'.format(800, 600)) #je geeft de grootte van de box (Tk) aan en met x en y

topFrame = Frame(root.configure(background="#FFCC00")) #je geeft de topframe een algemene kl
topFrame.pack(side=TOP) #je geeft aan dat de topframe wordt laten zien op de bovenste gedeelte van de box

bottomFrame = Frame(root) # een rechthoekig frame aanbrengen waar je widgets kan toevoegen/ je kan zelf de x en y bepalen
bottomFrame.pack(side=BOTTOM) # een frame aan de onderkant van het tkinter aanbrengen, hierdoor heb je dus ook gelijk een topframe

label1 = Label(root, height=3, font=TITLE_FONT,  text="Welkom bij NS", bg="#FFCC00", fg="#000066") #je geeft de label die je hebt aangemaakt een font, een achtergrond kleur en een fontkleur
label1.pack(fill=X) #je vult de hele x waarde/breedte van de label

label2 = Label(root, image=photo5,  bg="#00246B",  bd = 13,  anchor = W)
label2.pack(side = BOTTOM)

label3 = Label(root, image=photo1) #je zet een foto in de label waarvan je eerder de naam had gegeven
label3.pack(side=TOP)

    #Dit zijn de buttons die worden gebruikt voor de main menu

Button1 = Button(root, height = 5, width = 20, text="Ik wil naar Amsterdam", bg = "#00246B", fg ="white")
Button1.pack()
Button1.place(x=50, y=425)

Button2 = Button(root,height = 5, width = 20, text="Kopen los kaartje", bg = "#00246B", fg ="white")
Button2.pack()
Button2.place(x=225, y=425)

Button3 = Button(root,height = 5, width = 20, text="Kopen OV-chipkaart", bg = "#00246B", fg ="white") # hier moet een command
Button3.pack()
Button3.place(x=425, y=425)

Button4 = Button(root, height = 5, width = 20, text="Ik wil naar het buitenland", bg = "#00246B", fg ="white")
Button4.pack()
Button4.place(x=600, y=425)



root.mainloop() #een mainloop aan het scherm toevoegen zodat het scherm blijft runnen

#Ons probleem is dat we onze frame niet in een class kunnen zetten en dat we niet met een command kunnen overschakelen naar frame2