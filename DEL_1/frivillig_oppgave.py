import csv

MIN_TEMP = 5


def vekst_en_dag(temperatur):
    if temperatur < 0:
        return temperatur
    elif temperatur < MIN_TEMP:
        return 0
    else:
        return temperatur - MIN_TEMP

def maks_vekst(temperaturer, start):
    summen = 0
    maks = 0 
    for temperatur in temperaturer [start:]:
        summen += vekst_en_dag(temperatur)
        if summen > maks:
           maks = summen
    return maks

år = int(input("Skriv inn et årstall mellom 2014-2025: "))
datoer = []
temperaturer = []

with open("sinnes_2014_2025.csv", encoding="utf-8") as fil:
    leser = csv.reader(fil, delimiter=";")
    next(leser)
    for linje in leser:
        try:
            temperatur = float(linje[3].replace(",", "."))
        except (ValueError, IndexError):
            continue
        if linje[2].endswith(str(år)):
            datoer.append(linje[2])
            temperaturer.append(temperatur)

if len(temperaturer) == 0:
    print("Ingen data for dette året")
else:
        april = 0
        for i in range (len(datoer)):
            if ".04." in datoer[i]:
                april = i
            break
        print(f"Start 1. april: maksimal plantevekst er {maks_vekst(temperaturer, april):.1f}")

        beste_start = 0 
        beste_vekst = 0 
        for start in range (len(temperaturer)):
            vekst = maks_vekst(temperaturer, start)
            if vekst > beste_vekst:
                beste_start = start
                beste_vekst = vekst
        print(f"Beste startdato er {datoer[beste_start]} med maksimal plantevekst {beste_vekst:.1f}")