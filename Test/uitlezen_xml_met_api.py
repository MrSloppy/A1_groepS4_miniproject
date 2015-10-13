__author__ = 'Timo'


import requests                 # dit importeert de requests module die nodig is om toegang te krijgen tot de API
import codecs                   # dit inporteert de mogelijkheid om gebruik te maken van verschillende codecsen (gebruikt bij het uitlezen vande XML file)
import xmltodict                #Dit importeert de xmltodict module om xml bestanden in dictionaries te stoppen

# Deze gegevens worden naar de NS api gestuurd als authorisatie bij het request
auth_details = ("timovanetten@hotmail.com", "_Z-_9y12emNNuHaR2cPrYsCSqJInO2n1R3_RRyD-h3hpIUoeseM37w")

def Antwoord_API_van_Input():

    bestemming_input = input("Op welk Station bevind u zich?")
    # Dit is de request die je stuurt naar de API en het wordt opgeslagen in de variabele genaamd respons
    antwoord_API = requests.get("http://webservices.ns.nl/ns-api-avt?station={}".format(bestemming_input), auth=auth_details)

    # Dit print het gehele antwoord wat je van de API terug krijgt
    print(antwoord_API.text)

    # voor documenten zie functie beschrijving
    schrijf_xml(antwoord_API)

    # Dit stelt de dictionary stations_dict vast met de inhoud van antwoord_API.text
    # Iedere XML elemental is nu hierarchisch onderverdeeld in dictonaries
    stations_dict = xmltodict.parse(antwoord_API.text)

    # Deze loop loopt door de aangemaakte dictioanry stations_dict
    # en wanneer hij een element "ActueleVertrekTijden" ziet met een element "VertrekkendeTrein" erbij dan:
    try:
        for i in stations_dict["ActueleVertrekTijden"]["VertrekkendeTrein"]:
                # zet hij de informatie in dictionary i
                vertrekkende_trein=dict(i)
                print("Er vertrekt een trein met eindbestemming", vertrekkende_trein["EindBestemming"], " om:", vertrekkende_trein["VertrekTijd"][11:16])          # de vertrekkende_trein["VertrekTijd"][11:16] is nodig om alleen het uur en de minuten te printen en niet de rest

    except:
        print("Ongeldige invoer, probeer het opnieuw")



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

Antwoord_API_van_Input()
