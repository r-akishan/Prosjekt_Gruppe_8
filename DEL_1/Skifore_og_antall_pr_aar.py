# Oppgave e
filbane_makstemp = "sinnes_2014_2025_med_makstemperatur.csv"

def beregn_skifore(valgt_ar): 
    teller_skidager = 0 
    start_sesong = datetime.datetime(valgt_ar - 1, 11, 1) 
    slutt_sesong = datetime.datetime(valgt_ar, 5, 31) 
    hoyeste_dato_hittil = None 
    
    try:
        with open(filbane_makstemp, mode="r", encoding="utf-8") as fil:
            leser = csv.reader(fil, delimiter=";")
            next(leser) 
            
            for linje in leser:
                try:
                    dato = datetime.datetime.strptime(linje[2], "%d.%m.%Y") 
                except (ValueError, IndexError):
                    continue
                
                if start_sesong <= dato <= slutt_sesong: 
                    if hoyeste_dato_hittil and dato < hoyeste_dato_hittil: 
                        continue
                    hoyeste_dato_hittil = max(hoyeste_dato_hittil if hoyeste_dato_hittil else dato, dato)
                    
                    if len(linje) > 7:
                        snodybde = hent_tall(linje[7]) 
                        if snodybde is not None and snodybde >= 20: 
                            teller_skidager += 1
                            
        print(f"\ne) Skiføre i sesongen november {valgt_ar - 1} til mai {valgt_ar}:")
        print(f"   Antall dager med skiføre (>= 20cm snø): {teller_skidager} dager")
        
    except FileNotFoundError:
        print("Filen ble ikke funnet for oppgave e.")

arstall_e = int(input("Skriv inn et årstall for skiføre (2014 - 2025): "))
beregn_skifore(arstall_e)


# Oppgave h
filbane_makstemp = "sinnes_2014_2025_med_makstemperatur.csv"

def beregn_varme_dager(valgt_ar): 
    sommerdager = 0
    hoysommerdager = 0
    tropedager = 0
    hoyeste_dato_hittil = None
    
    try:
        with open(filbane_makstemp, mode="r", encoding="utf-8") as fil:
            leser = csv.reader(fil, delimiter=";")
            next(leser) 
            
            for linje in leser:
                try:
                    dato = datetime.datetime.strptime(linje[2], "%d.%m.%Y") 
                except (ValueError, IndexError):
                    continue
                
                if dato.year == valgt_ar: 
                    if hoyeste_dato_hittil and dato < hoyeste_dato_hittil: 
                        continue
                    hoyeste_dato_hittil = max(hoyeste_dato_hittil if hoyeste_dato_hittil else dato, dato)
                    
                    if len(linje) > 3:
                        maks_temp = hent_tall(linje[3]) 
                        
                        if maks_temp is not None:
                            if maks_temp > 30: 
                                tropedager += 1
                            elif maks_temp > 25: 
                                hoysommerdager += 1
                            elif maks_temp > 20: 
                                sommerdager += 1
                                
        print(f"\nh) Varme dager i kalenderåret {valgt_ar} (basert på makstemperatur):")
        print(f"   Antall sommerdager (20°C - 25°C): {sommerdager}")
        print(f"   Antall høysommerdager (25°C - 30°C): {hoysommerdager}")
        print(f"   Antall tropedager (>30°C): {tropedager}")
        
    except FileNotFoundError:
        print("Filen ble ikke funnet for oppgave h.")

arstall_h = int(input("Skriv inn et årstall for varme dager (2014 - 2025): "))
beregn_varme_dager(arstall_h)