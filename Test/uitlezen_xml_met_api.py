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



import xmltodict
stations_dict = xmltodict.parse(antwoord_API.text)
for i in stations_dict["ActueleVertrekTijden"]["VertrekkendeTrein"]:
    vertrekkende_trein=dict(i)
    print(vertrekkende_trein)