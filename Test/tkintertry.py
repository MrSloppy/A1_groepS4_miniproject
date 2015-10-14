__author__ = 'Timo'
__author__ = 'Plz no pasterino'

from tkinter import *
import requests                 # dit importeert de requests module die nodig is om toegang te krijgen tot de API
import codecs                   # dit inporteert de mogelijkheid om gebruik te maken van verschillende codecsen (gebruikt bij het uitlezen vande XML file)
import xmltodict                #Dit importeert de xmltodict module om xml bestanden in dictionaries te stoppen


# Deze gegevens worden naar de NS api gestuurd als authorisatie bij het request
auth_details = ("timovanetten@hotmail.com", "_Z-_9y12emNNuHaR2cPrYsCSqJInO2n1R3_RRyD-h3hpIUoeseM37w")

spoor_list = []
eindbestemming_list = []
vertrektijd_list = []
treinsoort_list = []

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


        lijst_met_stations.append(i["Namen"]["Lang"])      # Dit voegt het station toe aan de tuple

        lijst_met_stationcodes.append(i["Code"])                # Dit is de afkorting van  het station





def Antwoord_API_van_Input():

    bestemming_input = input("Op welk Station bevind u zich?")
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
        print("Ongeldige invoer, probeer het opnieuw")
        Antwoord_API_van_Input()



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

Antwoord_API_van_Input()                        # Dit voert de functie Antwoord_API_van_Input()

print(spoor_list)
print(treinsoort_list)
print(lijst_met_stationcodes)
from tkinter import Tk, StringVar, ttk

class Dropdown:

    def __init__(self, parent):
        self.parent = parent
        self.combo()

    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value,
                                state='readonly')

        self.box['values'] = (lijst_met_stations)
        self.box.current(0)
        self.box.grid(column=0, row=0)

if __name__ == '__main__':
    root = Tk()
    app = Dropdown(root)
    root.mainloop()

