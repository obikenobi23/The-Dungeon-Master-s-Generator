import openpyxl
from Encounters.Encounter import encounter
from Encounters.findMonster import findMonster


def createEncounter():
    # CR defineres
    crSpm = input("Hvilken vanskegrad vil du ha? ")
    diffBok = openpyxl.load_workbook("Encounters/DiffBok.xlsx")
    dSheet = diffBok.active

    # Leter etter riktig vanskegrad i bokens
    def lvlListe(liste):
        while True:
            heroLvl = input("Legg inn levelet til en helt:\n")
            print(heroLvl)
            if heroLvl == "":
                print("tom streng")
                return liste
            else:
                liste.append(int(heroLvl))

    lvler = lvlListe([])
    print(lvler)
    teamMembers = len(lvler)
    avgLvl = sum(lvler) / teamMembers
    column = 1
    for colNum in range(2, 6):
        if crSpm == dSheet.cell(1, colNum).value:
            column = colNum  # Angi hvilken vanskegrad maksExp skal hentes fra
            break

    # Definer maksimal exp for encounteret
    maxExp = teamMembers * dSheet.cell(avgLvl + 1, column).value
    print(maxExp)

    # Biome defineres
    def findBiomeList(liste):
        while True:
            biome = input("Hvilket miljø kjemper vi i? (0 for å avslutte) ")
            if biome == "":
                return liste
            else:
                liste.append(biome)
    biomeList = findBiomeList([])

    # Kjøre findMonster og encounter med parameter
    findMonster(biomeList)

    findMonster_list = findMonster(biomeList)
    validMonsters = findMonster_list[0]
    validMonsters_cr = findMonster_list[1]

    encounter(maxExp, validMonsters, validMonsters_cr)
