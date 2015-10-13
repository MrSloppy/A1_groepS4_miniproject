__author__ = 'Timo'


import requests                 # dit importeert de requests module die nodig is om toegang te krijgen tot de API

# Deze gegevens worden naar de NS api gestuurd als authorisatie bij het request
auth_details = ("timovanetten@hotmail.com", "_Z-_9y12emNNuHaR2cPrYsCSqJInO2n1R3_RRyD-h3hpIUoeseM37w")

# Dit is de request die je stuurt naar de API en het wordt opgeslagen in de variabele genaamd respons
antwoord_API = requests.get("http://webservices.ns.nl/ns-api-avt?station=ut", auth=auth_details)

# Dit print het gehele antwoord wat je van de API terug krijgt
print(antwoord_API.text)


# Nu we het antwoord van de API hebben gaan we dit opslaaan in een XML-bestand
#Hiervoor maken we de volgende functie aan


import codecs
def schrijf_xml(antwoord_API):

    # Hiermee wordt het bestand API_reposnse.mxl geöpend met schrijf bevoegdheid

    bestand = codecs.open("API_response.xml", 'w', 'utf-8')

    # Hiermee geef je het commando om het bestand met de volgende info te schrijven
    # namelijk de string variant van het antwoord wat we van de API kregej
    bestand.write(str(antwoord_API.text))

    # Vervolgens wordt het bestand gesloten zodat we niet perongeluk
    # het nog aanpassen als het open staat.
    bestand.close()

# Nu roepen we de fucntie aanmaken_xml aan:
schrijf_xml(antwoord_API)

bestemming_input = input("Wat is uw eindbestemming?")
#Dit importeert de xmltodict module om xml bestanden in dictionaries te stoppen
import xmltodict

# Dit stelt de dictionary stations_dict vast met de inhoud van antwoord_API.text
# Iedere XML elemental is nu hierarchisch onderverdeeld in dictonaries
stations_dict = xmltodict.parse(antwoord_API.text)

# Deze loop loopt door de aangemaakte dictioanry stations_dict
# en wanneer hij een element "ActueleVertrekTijden" ziet met een element "VertrekkendeTrein" erbij dan:
for i in stations_dict["ActueleVertrekTijden"]["VertrekkendeTrein"]:
    # zet hij de informatie in dictionary i
    vertrekkende_trein=dict(i)

    # De if statement die bepaald wanneer er geprint moet worden
    if vertrekkende_trein["EindBestemming"] == str(bestemming_input):
        # print vervolgens wanneer de if statement geldt worden de volgende gegevens geprint:
        print("Er vertrekt een trein met eindbestemming ", vertrekkende_trein["EindBestemming"], " om:", vertrekkende_trein["VertrekTijd"][11:16])          # de vertrekkende_trein["VertrekTijd"][11:16] is nodig om alleen het uur en de minuten te printen en niet de rest
