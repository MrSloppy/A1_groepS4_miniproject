from tkinter import * #tkinter GUI importen

root = Tk() #tkinter scherm aanmaken
TITLE_FONT = ("helvetica", 40, "bold") #

 #een foto toevoegen aan dit bestand
photo1 = PhotoImage( file="Welkomsttekst.png") # je geeft een PhotoImage file een variabele
photo2 = PhotoImage(file="Maestro.logo.png")
photo3 = PhotoImage(file="Master.Card.000.logo.png")
photo4 = PhotoImage(file="V.Pay.logo.png")
photo5 = PhotoImage(file="Bar.png")
photo6 = PhotoImage(file="Vlag.Verenigd.Koninkrijk.png")


root.resizable(width=FALSE, height=FALSE) #je geeft aaan dat je de root(Tk) niet kan veranderen qua grootte
root.geometry('{}x{}'.format(800, 600)) #je geeft de grootte van de box (Tk) aan en met x en y

topFrame = Frame(root.configure(background="#FFCC00")) #je geeft de topframe een algemene kleur
topFrame.pack(side=TOP) #je geeft aan dat de topframe wordt laten zien op de bovenste gedeelte van de box

bottomFrame = Frame(root) # een rechthoekig frame aanbrengen waar je widgets kan toevoegen/ je kan zelf de x en y bepalen
bottomFrame.pack(side=BOTTOM) # een frame aan de onderkant van het tkinter aanbrengen, hierdoor heb je dus ook gelijk een topframe

label1 = Label(root,height=3, font=TITLE_FONT,  text="Welkom bij NS", bg="#FFCC00", fg="#000066") #je geeft de label die je hebt aangemaakt een font, een achtergrond kleur en een fontkleur
label1.pack(fill=X)
label2 = Label(root, image=photo5,  bg="#00246B",  bd = 13,  anchor = W)
label2.pack(side = BOTTOM)

label3 = Label(root, image=photo1) #je zet een foto in de label waarvan je eerder de naam had gegeven
label3.pack(side=TOP)

root.mainloop() #een mainloop aan het scherm toevoegen zodat het scherm blijft runnen