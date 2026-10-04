#Oppgave e

filbane_makstemp = "Python-øvinger/Prosjekt_Gruppe_8/sinnes_2014_2025_med_makstemperatur.csv"

def beregn_skifore(valgt_ar):                                                                                   # Funksjon for å telle skiforedager i en sesong
    teller_skidager = 0                                                                                         # Teller for antall dager med skiføre
    start_sesong = datetime.datetime(valgt_ar - 1, 11, 1)                                                       # Skisesong starter 1. november året før
    slutt_sesong = datetime.datetime(valgt_ar, 5, 31)                                                           # Skisesong avsluttes 31. mai dette året
    hoyeste_dato_hittil = None                                                                                  # Sjekker om datoer hopper bakover i tid
    
    try:
        with open(filbane_makstemp, mode="r", encoding="utf-8") as fil:
            leser = csv.reader(fil, delimiter=";")
            next(leser)                                                                                         # Hopper over overskriften i filen
            
            for linje in leser:
                try:
                    dato = datetime.datetime.strptime(linje[2], "%d.%m.%Y")                                     # Konverterer tekst til datetime-objekt
                except (ValueError, IndexError):
                    continue
                
                if start_sesong <= dato <= slutt_sesong:                                                        # Sjekker om datoen er innenfor skisesongen
                    if hoyeste_dato_hittil and dato < hoyeste_dato_hittil:                                      # Forelesers tips: Forkaster feilsorterte linjer i sesongen
                        continue
                    hoyeste_dato_hittil = max(hoyeste_dato_hittil if hoyeste_dato_hittil else dato, dato)
                    
                    if len(linje) > 6:
                        snodybde = hent_tall(linje[6])                                                          # Henter snødybde fra kolonne 7
                        if snodybde is not None and snodybde >= 20:                                             # Sjekker kravet om minst 20 cm snø
                            teller_skidager += 1
                            
        print(f"\ne) Skiføre i sesongen november {valgt_ar - 1} til mai {valgt_ar}:")
        print(f"   Antall dager med skiføre (>= 20cm snø): {teller_skidager} dager")
        
    except FileNotFoundError:
        print("Filen ble ikke funnet for oppgave e.")

if gyldig_arstall:                                                                                              # Kjører funksjonen hvis årstallet er godkjent
    beregn_skifore(int(arstall))


#Oppgave h

filbane_makstemp = "Python-øvinger/Prosjekt_Gruppe_8/sinnes_2014_2025_med_makstemperatur.csv"

def beregn_varme_dager(valgt_ar):                                                                               # Funksjon for å telle varme dager i et år
    sommerdager = 0
    hoysommerdager = 0
    tropedager = 0
    hoyeste_dato_hittil = None
    
    try:
        with open(filbane_makstemp, mode="r", encoding="utf-8") as fil:
            leser = csv.reader(fil, delimiter=";")
            next(leser)                                                                                         # Hopper over overskriften i filen
            
            for linje in leser:
                try:
                    dato = datetime.datetime.strptime(linje[2], "%d.%m.%Y")                                     # Konverterer tekst til datetime-objekt
                except (ValueError, IndexError):
                    continue
                
                if dato.year == valgt_ar:                                                                       # Sjekker om datoen tilhører det valgte kalenderåret
                    if hoyeste_dato_hittil and dato < hoyeste_dato_hittil:                                      # Forelesers tips: Forkaster feilsorterte linjer i året
                        continue
                    hoyeste_dato_hittil = max(hoyeste_dato_hittil if hoyeste_dato_hittil else dato, dato)
                    
                    if len(linje) > 7:
                        maks_temp = hent_tall(linje[7])                                                         # Henter makstemperatur fra kolonne 8
                        
                        if maks_temp is not None:
                            if maks_temp > 30:                                                                  # Tropedag: over 30 grader
                                tropedager += 1
                            elif maks_temp > 25:                                                                # Høysommerdag: over 25 grader (og under 30)
                                hoysommerdager += 1
                            elif maks_temp > 20:                                                                # Sommerdag: over 20 grader (og under 25)
                                sommerdager += 1
                                
        print(f"\nh) Varme dager i kalenderåret {valgt_ar} (basert på makstemperatur):")
        print(f"   Antall sommerdager (20°C - 25°C): {sommerdager}")
        print(f"   Antall høysommerdager (25°C - 30°C): {hoysommerdager}")
        print(f"   Antall tropedager (>30°C): {tropedager}")
        
    except FileNotFoundError:
        print("Filen ble ikke funnet for oppgave h.")

if gyldig_arstall:                                                                                              # Kjører funksjonen hvis årstallet er godkjent
    beregn_varme_dager(int(arstall))
