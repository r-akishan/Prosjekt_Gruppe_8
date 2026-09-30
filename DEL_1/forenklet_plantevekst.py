#oppgave f
import csv

MIN_TEMP = 5

def vekst_en_dag(temperatur):
    vekst = temperatur - MIN_TEMP
    if vekst < 0:
        return 0
    else:
        return vekst

def total_vekst(år):
    total = 0
    dager = 0

    with open("sinnes_2014_2025.csv", mode="r", encoding="utf-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser)

        for linje in leser:
            try:
                linje_år = int(linje[2].split(".")[2])
                temperatur = float(linje[3].replace(",", "."))
            except (ValueError, IndexError):
                continue

            if linje_år == år:
                total += vekst_en_dag(temperatur)
                dager += 1

    return total, dager

år = int(input("Skriv inn et årstall mellom 2014-2026 :"))
vekst, dager = total_vekst(år)
print(f"Planten vokste {vekst:.1f} vekstenheter i {år} i løpet av {dager} dager.")
        
