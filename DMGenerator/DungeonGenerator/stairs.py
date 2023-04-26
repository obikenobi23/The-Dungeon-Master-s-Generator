import openpyxl
import random


def stairs():
    # Opprett kontakt med excel
    wb = openpyxl.load_workbook("DungeonGenerator/DungeonParts.xlsx")
    sheet = wb.sheetnames[4]

    # Hent en streng fra tabellen og skriv den ut
    diceRoll = random.randrange(1, 21)
    stairType = wb[sheet].cell(diceRoll, 1).value.lower()
    if diceRoll in range(1, 17):
        print("The stairs leads {}.".format(stairType))
    elif diceRoll in range(17, 21):
        print("There is an opening in the wall: a {}.".format(stairType))
