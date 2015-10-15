__author__ = 'Timo'
__author__ = 'Plz no pasterino'
#version:0.0

from tkinter import *
import requests                 # dit importeert de requests module die nodig is om toegang te krijgen tot de API
import codecs                   # dit inporteert de mogelijkheid om gebruik te maken van verschillende codecsen (gebruikt bij het uitlezen vande XML file)
import xmltodict                #Dit importeert de xmltodict module om xml bestanden in dictionaries te stoppen


# Deze gegevens worden naar de NS api gestuurd als authorisatie bij het request
auth_details = ("timovanetten@hotmail.com", "_Z-_9y12emNNuHaR2cPrYsCSqJInO2n1R3_RRyD-h3hpIUoeseM37w")

global spoor_list
spoor_list = []
global eindbestemming_list
eindbestemming_list = []
global vertrektijd_list
vertrektijd_list = []
global treinsoort_list
treinsoort_list = []
global station_keuze_voor_gegevens

bestemming_input = "Test"


# Deze fuctie is geschreven om een lijst met alle stations en schrijftypes in te vullen in een tuple
def Stations_Lijst_Maken():

    # Dit is de request die je stuurt naar de API en het wordt opgeslagen in de variabele genaamd antwoord_API
    antwoord_API = requests.get("http://webservices.ns.nl/ns-api-stations-v2", auth=auth_details)
    print(antwoord_API.text)                            # Een printje om te kijken of het request goed is geretouneerd
    schrijf_xml(antwoord_API)                           # dit roept de functie schrijf_xml met de parameter antwoord_API aan
    stations_dict = xmltodict.parse(antwoord_API.text)
    global lijst_met_stations                           # dit maakt de lijst_met_stations globaal zodat hij later nog kan worden aangeroepen
    lijst_met_stations = []                          # Dit is de lege set die zo gevuld gaat worden
    global lijst_met_stationcodes
    lijst_met_stationcodes = []
    for i in stations_dict["Stations"]["Station"]:      # Dit is de loop die door alle verzamelde informatie gaat onder de dictionaries ["Stations"]["Station"]
        if (i["Land"]) == "NL":
            lijst_met_stations.append(i["Namen"]["Lang"])      # Dit voegt het station toe aan de tuple

            lijst_met_stationcodes.append(i["Code"])                # Dit is de afkorting van  het station






def Antwoord_API_van_Input():
    global bestemming_input
    bestemming_input = "Utrecht Centraal"
    # Dit is de request die je stuurt naar de API en het wordt opgeslagen in de variabele genaamd antwoord_API
    code_van_station = lijst_met_stations.index(bestemming_input)
    station_code = lijst_met_stationcodes[code_van_station]
    antwoord_API = requests.get("http://webservices.ns.nl/ns-api-avt?station={}".format(station_code), auth=auth_details)

    # Dit print het gehele antwoord wat je van de API terug krijgt
    print(antwoord_API.text)

    # voor documenten zie functie beschrijving
    schrijf_xml(antwoord_API)

    # Dit stelt de dictionary stations_dict vast met de inhoud van antwoord_API.text
    # Iedere XML elemental is nu hierarchisch onderverdeeld in dictonaries
    global stations_dict
    stations_dict = xmltodict.parse(antwoord_API.text)

    # Deze loop loopt door de aangemaakte dictioanry stations_dict
    # en wanneer hij een element "ActueleVertrekTijden" ziet met een element "VertrekkendeTrein" erbij dan:
    try:
        for i in stations_dict["ActueleVertrekTijden"]["VertrekkendeTrein"]:
                # zet hij de informatie in dictionary i
                vertrekkende_trein=dict(i)

                # Hier worden wat variabele vast gelegd voor gebruiksgemak voor later
                global eindbestemming
                eindbestemming = vertrekkende_trein["EindBestemming"]
                global vertrektijd
                vertrektijd = vertrekkende_trein["VertrekTijd"][11:16]          # de vertrekkende_trein["VertrekTijd"][11:16] is nodig om alleen het uur en de minuten te printen en niet de rest
                global treinsoort
                treinsoort = vertrekkende_trein["TreinSoort"]
                global spoor
                spoor = vertrekkende_trein["VertrekSpoor"]["#text"]
                global afkorting


                # Hier worden de dictionaries gevuld om voor later gebruik in de GUI
                global eindbestemming_list
                eindbestemming_list.append(eindbestemming)
                global vertrektijd_list
                vertrektijd_list.append(vertrektijd)
                global treinsoort_list
                treinsoort_list.append(treinsoort)
                global spoor_list
                spoor_list.append(spoor)

                print("Er vertrekt een trein met eindbestemming", eindbestemming, " om:", vertrektijd)          # Dit print de gevraagde informatie
                print("Het type van deze trein is: ", treinsoort, " en deze vertrekt vanaf spoor", spoor)       # Dit print de rest van de gevraagde informatie

    except:
        pass


#d[ogbjsofiuns

# Nu we het antwoord van de API hebben gaan we dit opslaaan in een XML-bestand
#Hiervoor maken we de volgende functie aan
def schrijf_xml(antwoord_API):

    # Hiermee wordt het bestand API_reposnse.mxl geöpend met schrijf bevoegdheid
    bestand = codecs.open("API_response.xml", 'w', 'utf-8')

    # Hiermee geef je het commando om het bestand met de volgende info te schrijven
    # namelijk de string variant van het antwoord wat we van de API kregej
    bestand.write(str(antwoord_API.text))

    # Vervolgens wordt het bestand gesloten zodat we niet perongeluk
    # het nog aanpassen als het open staat.
    bestand.close()

Stations_Lijst_Maken()                          # dit roept de functie aan om de grote tuple van Stations aan te maken
print(lijst_met_stations)                       # dit print de lijst_met_stations om te checken of het aanmaken goed gegaan is
print(len(lijst_met_stations))                  # dit print de lengte van de lijst_met_stations

print(spoor_list)
print(treinsoort_list)
print(lijst_met_stationcodes)

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
    Antwoord_API_van_Input()

    master = Tk()
    master.resizable(width=0, height=0)
    master.geometry("800x600")
    master.config(bg="gold")

    Gfont=("helvetica", 40, "bold")
    Buttonfont=("helvetica", 16)

    label_weergave1 = Label(master, text = "Tijd", bg="gold")
    label_weergave1.place(x=200, y=100)

    label_weergave2 = Label(master, text = "Station", bg="gold")
    label_weergave2.place(x=250, y=100)

    label_weergave3 = Label(master, text = "Type Trein",  bg="gold")
    label_weergave3.place(x=430, y=100)

    label_weergave4 = Label(master, text = "Spoor", bg="gold")
    label_weergave4.place(x=600, y=100)



    label_huidig_station = Label(master, bg="gold", text = "{}".format(bestemming_input))
    label_huidig_station.place(x=100, y=100)
    label_Tijd0 = Label(master, bg="gold", text = "{}".format(vertrektijd_list[0]))
    label_Tijd0.place(x = 200, y= 150 )
    label_Eindbestemming0 = Label(master, bg="gold", text = "{}".format(eindbestemming_list[0]))
    label_Eindbestemming0.place(x = 250, y = 150)
    label_Spoor0 = Label(master,  bg="gold",text = "{}".format(spoor_list[0]))
    label_Spoor0.place(x = 600, y = 150)
    label_Typetrein0 = Label(master,  bg="gold",text = "{}".format(treinsoort_list[0]))
    label_Typetrein0.place(x= 430, y = 150)

    label_Tijd1 = Label(master, bg="gold", text = "{}".format(vertrektijd_list[1]))
    label_Tijd1.place(x = 200, y= 250 )
    label_Eindbestemming1 = Label(master, bg="gold", text = "{}".format(eindbestemming_list[1]))
    label_Eindbestemming1.place(x = 250, y = 250)
    label_Spoor1 = Label(master, bg="gold", text = "{}".format(spoor_list[1]))
    label_Spoor1.place(x = 600, y = 250)
    label_Typetrein1 = Label(master,  bg="gold",text = "{}".format(treinsoort_list[1]))
    label_Typetrein1.place(x= 430, y = 250)

    label_Tijd2 = Label(master,  bg="gold",text = "{}".format(vertrektijd_list[2]))
    label_Tijd2.place(x = 200, y= 350 )
    label_Eindbestemming2 = Label(master, bg="gold", text = "{}".format(eindbestemming_list[2]))
    label_Eindbestemming2.place(x = 250, y = 350)
    label_Spoor2 = Label(master, bg="gold", text = "{}".format(spoor_list[2]))
    label_Spoor2.place(x = 600, y = 350)
    label_Typetrein2 = Label(master, bg="gold", text = "{}".format(treinsoort_list[2]))
    label_Typetrein2.place(x= 430, y = 350)

    label_Tijd3 = Label(master, bg="gold", text = "{}".format(vertrektijd_list[3]))
    label_Tijd3.place(x = 200, y= 450 )
    label_Eindbestemming3 = Label(master, bg="gold", text = "{}".format(eindbestemming_list[3]))
    label_Eindbestemming3.place(x = 250, y = 450)
    label_Spoor3 = Label(master, bg="gold", text = "{}".format(spoor_list[3]))
    label_Spoor3.place(x = 600, y = 450)
    label_Typetrein3 = Label(master, bg="gold", text = "{}".format(treinsoort_list[3]))
    label_Typetrein3.place(x= 430, y = 450)

def venster4(event):
    global var
    var = StringVar(root)
    global Optie_menu
    Optie_menu = OptionMenu(root, var, *lijst_met_stations)
    var.set("Uw Station")
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000, y=1000)
    Optie_menu.pack()
    Optie_menu.place(x = 350, y = 300)

    print(var.get())

    AnderStation.pack()
    def ok():
        spoor_list = []
        eindbestemming_list = []
        vertrektijd_list = []
        treinsoort_list = []
        vertrekkende_trein= []
        print(var.get())

        station_keuze_voor_gegevens = var.get()

        code_van_station = lijst_met_stations.index(var.get())
        station_code = lijst_met_stationcodes[code_van_station]
        print(station_code)
        print("value is", var.get())
        antwoord_API = requests.get("http://webservices.ns.nl/ns-api-avt?station={}".format(var.get()), auth=auth_details)

        # Dit print het gehele antwoord wat je van de API terug krijgt
        # voor documenten zie functie beschrijving
        schrijf_xml(antwoord_API)

        # Dit stelt de dictionary stations_dict vast met de inhoud van antwoord_API.text
        # Iedere XML elemental is nu hierarchisch onderverdeeld in dictonaries
        global stations_dict
        stations_dict = xmltodict.parse(antwoord_API.text)

        # Deze loop loopt door de aangemaakte dictioanry stations_dict
        # en wanneer hij een element "ActueleVertrekTijden" ziet met een element "VertrekkendeTrein" erbij dan:

        for i in stations_dict["ActueleVertrekTijden"]["VertrekkendeTrein"]:
            # zet hij de informatie in dictionary i
            vertrekkende_trein=dict(i)

            # Hier worden wat variabele vast gelegd voor gebruiksgemak voor later
            global eindbestemming
            eindbestemming = vertrekkende_trein["EindBestemming"]
            global vertrektijd
            vertrektijd = vertrekkende_trein["VertrekTijd"][11:16]          # de vertrekkende_trein["VertrekTijd"][11:16] is nodig om alleen het uur en de minuten te printen en niet de rest
            global treinsoort
            treinsoort = vertrekkende_trein["TreinSoort"]
            global spoor
            spoor = vertrekkende_trein["VertrekSpoor"]["#text"]
            global afkorting


            # Hier worden de dictionaries gevuld om voor later gebruik in de GUI

            eindbestemming_list.append(eindbestemming)

            vertrektijd_list.append(vertrektijd)

            treinsoort_list.append(treinsoort)

            spoor_list.append(spoor)
            print(vertrektijd_list)

            print("Er vertrekt een trein met eindbestemming", eindbestemming, " om:", vertrektijd)          # Dit print de gevraagde informatie
            print("Het type van deze trein is: ", treinsoort, " en deze vertrekt vanaf spoor", spoor)       # Dit print de rest van de gevraagde informatie

    global Button9
    Button9 = Button(root, wraplength=125, justify=LEFT, text="Bevestig",bg = "#00246B", fg = "white",font = Buttonfont, width=10, command=ok)
    Button9.bind('<Button-1>', venster5)
    Button9.pack()
    Button9.place(x=170,y=450)


def venster5(event):
    print(var.get())
    master = Tk()
    AnderStation.pack()
    spoor_list = []
    eindbestemming_list = []
    vertrektijd_list = []
    treinsoort_list = []
    vertrekkende_trein= []

    antwoord_API = requests.get("http://webservices.ns.nl/ns-api-avt?station={}".format(var.get()), auth=auth_details)

    # Dit print het gehele antwoord wat je van de API terug krijgt
    # voor documenten zie functie beschrijving
    schrijf_xml(antwoord_API)

    # Dit stelt de dictionary stations_dict vast met de inhoud van antwoord_API.text
    # Iedere XML elemental is nu hierarchisch onderverdeeld in dictonaries
    global stations_dict
    stations_dict = xmltodict.parse(antwoord_API.text)

    # Deze loop loopt door de aangemaakte dictioanry stations_dict
    # en wanneer hij een element "ActueleVertrekTijden" ziet met een element "VertrekkendeTrein" erbij dan:

    for i in stations_dict["ActueleVertrekTijden"]["VertrekkendeTrein"]:
        # zet hij de informatie in dictionary i
        vertrekkende_trein=dict(i)

        # Hier worden wat variabele vast gelegd voor gebruiksgemak voor later
        global eindbestemming
        eindbestemming = vertrekkende_trein["EindBestemming"]
        global vertrektijd
        vertrektijd = vertrekkende_trein["VertrekTijd"][11:16]          # de vertrekkende_trein["VertrekTijd"][11:16] is nodig om alleen het uur en de minuten te printen en niet de rest
        global treinsoort
        treinsoort = vertrekkende_trein["TreinSoort"]
        global spoor
        spoor = vertrekkende_trein["VertrekSpoor"]["#text"]
        global afkorting


        # Hier worden de dictionaries gevuld om voor later gebruik in de GUI

        eindbestemming_list.append(eindbestemming)

        vertrektijd_list.append(vertrektijd)

        treinsoort_list.append(treinsoort)

        spoor_list.append(spoor)
        print(vertrektijd_list)

        print("Er vertrekt een trein met eindbestemming", eindbestemming, " om:", vertrektijd)          # Dit print de gevraagde informatie
        print("Het type van deze trein is: ", treinsoort, " en deze vertrekt vanaf spoor", spoor)       # Dit print de rest van de gevraagde informatie


    master.resizable(width=0, height=0)
    master.geometry("800x600")
    master.config(bg="gold")


    label_weergave4 = Label(master, text = "Tijd:", bg ="gold")
    label_weergave4.place(x = 200, y = 100)
    label_weergave5 = Label(master, text = "Station", bg = "gold")
    label_weergave5.place(x = 250, y = 100)
    label_weergave6 = Label(master, text = "Type trein", bg = "gold")
    label_weergave6.place(x = 430, y = 100)
    label_weergave7 = Label(master, text = "Spoor",bg = "gold")
    label_weergave7.place(x = 600, y = 100)


    label_huidig_station = Label(master, text = "{}".format(var.get()), bg = "gold")
    label_huidig_station.place(x=100, y=100)
    label_Tijd0 = Label(master, text = "{}".format(vertrektijd_list[0]), bg = "gold")
    label_Tijd0.place(x = 200, y= 150 )
    label_Eindbestemming0 = Label(master, text = "{}".format(eindbestemming_list[0]), bg = "gold")
    label_Eindbestemming0.place(x = 250, y = 150)
    label_Spoor0 = Label(master, text = "{}".format(spoor_list[0]), bg = "gold")
    label_Spoor0.place(x = 600, y = 150)
    label_Typetrein0 = Label(master, text = "{}".format(treinsoort_list[0]), bg = "gold")
    label_Typetrein0.place(x= 430, y = 150)

    label_Tijd1 = Label(master, text = "{}".format(vertrektijd_list[1]), bg = "gold")
    label_Tijd1.place(x = 200, y= 250 )
    label_Eindbestemming1 = Label(master, text = "{}".format(eindbestemming_list[1]), bg = "gold")
    label_Eindbestemming1.place(x = 250, y = 250)
    label_Spoor1 = Label(master, text = "{}".format(spoor_list[1]), bg = "gold")
    label_Spoor1.place(x = 600, y = 250)
    label_Typetrein1 = Label(master, text = "{}".format(treinsoort_list[1]), bg = "gold")
    label_Typetrein1.place(x= 430, y = 250)

    label_Tijd2 = Label(master, text = "{}".format(vertrektijd_list[2]), bg = "gold")
    label_Tijd2.place(x = 200, y= 350 )
    label_Eindbestemming2 = Label(master, text = "{}".format(eindbestemming_list[2]), bg = "gold")
    label_Eindbestemming2.place(x = 250, y = 350)
    label_Spoor2 = Label(master, text = "{}".format(spoor_list[2]), bg = "gold")
    label_Spoor2.place(x = 600, y = 350)
    label_Typetrein2 = Label(master, text = "{}".format(treinsoort_list[2]), bg = "gold")
    label_Typetrein2.place(x= 430, y = 350)

    label_Tijd3 = Label(master, text = "{}".format(vertrektijd_list[3]), bg = "gold")
    label_Tijd3.place(x = 200, y= 450 )
    label_Eindbestemming3 = Label(master, text = "{}".format(eindbestemming_list[3]), bg = "gold")
    label_Eindbestemming3.place(x = 250, y = 450)
    label_Spoor3 = Label(master, text = "{}".format(spoor_list[3]), bg = "gold")
    label_Spoor3.place(x = 600, y = 450)
    label_Typetrein3 = Label(master, text = "{}".format(treinsoort_list[3]), bg = "gold")
    label_Typetrein3.place(x= 430, y = 450)


def reset(event):
    try:
        Optie_menu.forget()
        Button9.forget()
    except:
        pass
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
    try:
        Optie_menu.place(x=1000, y=1000)
    except:
        pass
    label2.pack(side=BOTTOM)
    Button8.place(x=1000,y=1000)
    HuidigStation.pack_forget()
    AnderStation.pack_forget()

def venster1():
    try:
        Optie_menu.forget()
    except:
        pass

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
    global Button_A
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




    root.mainloop()



venster1()