import csv                                                                                                      # Importerer csv funksjon for å åpne csv-fil
import datetime                                                                                                 # Importerer datetime for å vise til hva som er dd,mm og åååå
import matplotlib.pyplot as plt                                                                                 # Importerer pyplot for å tegne digrammer, grafer osv.
import matplotlib.ticker as ticker                                                                              # Importerer ticker for å legge grader, mm, cm, m/s

try:
    while True:                                                                                                 # Lager en while-løkke som ikke går videre før brukeren skriver riktig årstall
        arstall = input("Skriv inn et årstall (2014 - 2025): ").strip()
        if len(arstall) != 4 or arstall.isdigit() == False:                                                     # Sjekker om det er 4 tegn og om de tegnene er tall
            print("Ikke glem å skriv inn et årstall!")
        elif int(arstall) < 2014 or int(arstall) > 2025:                                                        # Sjekker om brukerer har skrevet et årstall mellom 2014 og 2025
            print("Vennligst skriv et årstall mellom 2014 og 2025!")
        else:
            break
                                                                                                                # Lager lister for de ulike værobservasjonene
    dag_x = [] 
    mt = []
    nb = []
    hm = []
    sd = []
    gyldig_arstall = False
    def hent_tall(tall):                                                                                        # Lager en funksjon som gjør om , til . og samtidig sjekker om det kan gjøres om til desimaltall
        try:
            konverter = float(tall.replace(",", "."))
            return konverter
        except:
            konverter = None
            return konverter

    with open("Python-øvinger/Prosjekt_Gruppe_8/sinnes_2014_2025.csv", mode = "r", encoding = "utf-8") as fil:  # Åpner csv-filen ved bruk av with open()

        leser = csv.reader(fil, delimiter = ";")                                                                # Leser gjennom filen og viser til at det er delt i flere kolonner ved bruk av ;
        overskrift = next(leser)                                                                                # Hopper over første linjen i csv-filen
        
        for linje in leser:                                                                                     # Lager en for-løkke som leser gjennom csv-filen linje for linje
            try:
                dato = datetime.datetime.strptime(linje[2], "%d.%m.%Y")                                         # Brukter funksjonen datetime for å vise til hvilken format datoen har
                if gyldig_arstall and dato.year != int(arstall):                                                # Sjekker om det allerede er funnet årstallet og om årstallet har endret seg
                    break
            except ValueError:
                continue
            if len(linje) > 3 and dato.year == int(arstall):                                                    # Sjekker om linjen har nok elementer og om årstallet er lik brukerens årstall
                gyldig_arstall = True                                                                           # Setter = True og bruker funksjonen til å definerer kolonnene i csv-filen      
                middeltemperatur = hent_tall(linje[3])
                nedbor = hent_tall(linje[4])
                if nedbor == None:                                                                              # Sjekker om nedbør = None og gjør om til 0, plt.bar tar ikke imot når en verdi er None
                    nedbor = 0
                hoyeste_middelvind = hent_tall(linje[5])
                snodybde = hent_tall(linje[6])
                mt.append(middeltemperatur)                                                                     # Setter alle kolonnene inn i sin egen liste
                nb.append(nedbor)
                hm.append(hoyeste_middelvind)
                sd.append(snodybde)
                dag_x.append(dato)                                                                              # Setter alle datoene i løpet av et år i en egen liste
                

    if not gyldig_arstall:                                                                                      # Sjekker om brukerens årstall er gyldig
        print("Fant ingen data for det årstallet!")
    else:
        fig, akser = plt.subplots(2, 2, figsize = (13, 7))                                                      # Lager 4 ulike figurer der hver akse representerer en figur
        fig.autofmt_xdate(rotation = 45)                                                                        # Roterer x-aksen 45 grader, altså datoene
        fig.suptitle(f"Sinnes værstasjon i Sirdalen {arstall}")                                                 # Felles overskrift for alle 4 figurene
        akser[0, 0].plot(dag_x, mt, label = "Middeltemperatur")                                                 # Første figur
        akser[0, 0].set_title("Middeltemperatur")
        akser[0, 0].yaxis.set_major_formatter(ticker.FormatStrFormatter("%g°C"))                                # Legger inn måleenheter, %g er tallet som skal så før måleenheten
        akser[0, 0].grid(True)
        akser[0, 1].plot(dag_x, hm, label = "Høyeste-middelvind")                                               # Andre figur
        akser[0, 1].set_title("Høyeste-middelvind")
        akser[0, 1].yaxis.set_major_formatter(ticker.FormatStrFormatter("%gm/s"))                               # Legger inn måleenheter, %g er tallet som skal så før måleenheten
        akser[0, 1 ].grid(True)
        akser[1, 0].plot(dag_x, sd, label = "Snødybde")                                                         # Tredje figur
        akser[1, 0].set_title("Snødybde")
        akser[1, 0].yaxis.set_major_formatter(ticker.FormatStrFormatter("%gcm"))                                # Legger inn måleenheter, %g er tallet som skal så før måleenheten
        akser[1, 0 ].grid(True)
        akser[1, 1].bar(dag_x, nb, label = "Nedbør")                                                            # Fjerde figur
        akser[1, 1].set_title("Nedbør")
        akser[1, 1].yaxis.set_major_formatter(ticker.FormatStrFormatter("%gmm"))                                # Legger inn måleenheter, %g er tallet som skal så før måleenheten
        akser[1, 1 ].grid(True)
        plt.tight_layout()
        plt.show()

except FileNotFoundError:
    print("Filen er ikke eksisterende.")                
