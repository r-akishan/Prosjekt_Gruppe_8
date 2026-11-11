import csv                                                                                                      # Importerer csv funksjon for å åpne csv-fil
import datetime                                                                                                 # Importerer datetime for å vise til hva som er dd,mm og åååå
import matplotlib.pyplot as plt                                                                                 # Importerer pyplot for å tegne digrammer, grafer osv.
import matplotlib.ticker as ticker                                                                              # Importerer ticker for å legge grader, mm, cm, m/s

try:
    dag_x = [] 
    maks_mt = []
    min_mt = []
    nb = []
    mv = []
    sd = []
    def hent_tall(tall):                                                                                        # Lager en funksjon som gjør om , til . og samtidig sjekker om det kan gjøres om til desimaltall
        try:
            konverter = float(tall.replace(",", "."))
            return konverter
        except:
            konverter = None
            return konverter

    with open("Python-øvinger/Prosjekt_Gruppe_8/DEL_2/flere_vaerstasjoner_med_makstemperatur/oslo_blindern_1954_2025_med_makstemperatur.csv", mode = "r", encoding = "utf-8") as fil:  # Åpner csv-filen ved bruk av with open()

        leser = csv.reader(fil, delimiter = ";")                                                                # Leser gjennom filen og viser til at det er delt i flere kolonner ved bruk av ;
        overskrift = next(leser)                                                                                # Hopper over første linjen i csv-filen

        forrige_maaned = None
        forrige_aar = None
        maaned_total_nb = 0
        maaned_telle_nb = 0
        maaned_maks_sd = None
        maaned_maks_mt = None
        maaned_min_mt = None
        maaned_maks_mv = None
        
        for linje in leser:                                                                                     # Lager en for-løkke som leser gjennom csv-filen linje for linje
            try:
                dato = datetime.datetime.strptime(linje[2], "%d.%m.%Y")                                         # Brukter funksjonen datetime for å vise til hvilken format datoen har
            except ValueError:
                continue
            naavarende_maaned = dato.month
            naavarende_aar = dato.year
            
            if forrige_maaned is not None and (naavarende_maaned != forrige_maaned or naavarende_aar != forrige_aar):

                if maaned_telle_nb > 20:
                    nb.append(maaned_total_nb)
                else:
                    nb.append(0)
            
                maks_mt.append(maaned_maks_mt)                                                                     # Setter alle kolonnene inn i sin egen liste
                min_mt.append(maaned_min_mt)
                mv.append(maaned_maks_mv)
                sd.append(maaned_maks_sd)
                dag_x.append(datetime.datetime(forrige_aar, forrige_maaned, 1))                                                                              # Setter alle datoene i løpet av et år i en egen liste

                maaned_total_nb = 0
                maaned_telle_nb = 0
                maaned_maks_sd = None
                maaned_maks_mt = None
                maaned_min_mt = None
                maaned_maks_mv = None
                
            forrige_maaned = naavarende_maaned
            forrige_aar = naavarende_aar

            dagens_nb = hent_tall(linje[4])
            dagens_mt = hent_tall(linje[3])
            dagens_sd = hent_tall(linje[6])
            dagens_mv = hent_tall(linje[5])

            if dagens_nb is not None:
                maaned_total_nb += dagens_nb
                maaned_telle_nb += 1

            if dagens_mt is not None:
                if maaned_maks_mt is None:
                    maaned_maks_mt = dagens_mt
                    maaned_min_mt = dagens_mt
                else:
                    maaned_maks_mt = max(maaned_maks_mt, dagens_mt)
                    maaned_min_mt = min(maaned_min_mt, dagens_mt)
                

            if dagens_sd is not None:
                if maaned_maks_sd is None:
                    maaned_maks_sd = dagens_sd
                else:
                    maaned_maks_sd = max(maaned_maks_sd, dagens_sd)

            if dagens_mv is not None:
                if maaned_maks_mv is None:
                    maaned_maks_mv = dagens_mv
                else:
                    maaned_maks_mv = max(maaned_maks_mv, dagens_mv)

        if forrige_maaned is not None:
            if maaned_telle_nb > 20:
                nb.append(maaned_total_nb)
            else:
                nb.append(0)
            maks_mt.append(maaned_maks_mt)
            min_mt.append(maaned_min_mt)
            mv.append(maaned_maks_mv)
            sd.append(maaned_maks_sd)
            dag_x.append(datetime.datetime(forrige_aar, forrige_maaned, 1))

    if len(dag_x) == 0:                                                                                      # Sjekker om brukerens årstall er gyldig
        print("Fant ingen data for det årstallet!")
    else:
        fig, akser = plt.subplots(2, 2, figsize = (13, 7))                                                      # Lager 4 ulike figurer der hver akse representerer en figur
        fig.autofmt_xdate(rotation = 45)                                                                        # Roterer x-aksen 45 grader, altså datoene
        fig.suptitle("--- ")                                                 # Felles overskrift for alle 4 figurene
        akser[0, 0].plot(dag_x, maks_mt, label = "Maks Middeltemperatur")                                                 # Første figur
        akser[0, 0].plot(dag_x, min_mt, label = "Min Middeltemperatur")
        akser[0, 0].set_title("Middeltemperatur")
        akser[0, 0].yaxis.set_major_formatter(ticker.FormatStrFormatter("%g°C"))                                # Legger inn måleenheter, %g er tallet som skal så før måleenheten
        akser[0, 0].grid(True)
        akser[0, 0].legend()
        akser[0, 1].plot(dag_x, mv, label = "Høyeste-middelvind")                                               # Andre figur
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
