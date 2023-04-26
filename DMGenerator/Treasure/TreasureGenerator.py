import openpyxl
import random
import sys

# Introduserer Excel
wb = openpyxl.load_workbook('Treasure/TreasureChart.xlsx')
sheet = wb.sheetnames[0]


def treasure(type, cr):
    treasureRoll = random.randrange(1, 101)  # diceroll

    diceString = ""  # Kun for å fikse feilmelding
    # Henter ut streng fra arket
    if type == "loot":
        diceString = lootRoll(cr, treasureRoll)
    elif type == "hoard":
        diceString = hoardRoll(cr, treasureRoll)
    else:
        print("Galt input: treasure() -- Ikke \"loot\" eller \"hoard\".")
        exit(2)

    print(diceString)


def findCell(cr, treasureRoll, rangemax):
    # Introduserer Excel
    # wb = openpyxl.load_workbook('Treasure/TreasureChart.xlsx')
    # sheet = wb.sheetnames[0]
    column = cr

    for i in range(1, rangemax + 1):
        tryTable = wb[sheet].cell(i, column).value
        inBetweens = tryTable.split(",")
        lower = int(inBetweens[0])
        upper = int(inBetweens[1])
        if treasureRoll in range(lower, upper):
            lootDiceString = wb[sheet].cell(i, column + 1).value
            return lootDiceString
    print("findCell fant ikke riktig rute")
    exit(2)


def findCellHoard(cr, treasureRoll):
    column = cr

    lootDiceString = wb[sheet].cell(treasureRoll, column + 1).value
    return lootDiceString


def rollDice(rollAmount, rollSize, multiplier):
    totalt = 0
    for i in range(rollAmount):
        totalt += random.randint(1, rollSize)
    totalt = totalt * multiplier
    return totalt


def equationSeparatorCash(characters):
    # string = KP:4d6x100;GP:1d6x5
    # Må fungere parallelt på ett og to elementer. Noen har to deler med semikolon-separator, andre har ikke.
    string = ""
    for character in characters:
        string += str(character)
    if ";" in string:
        string = string.split(";")
    else:
        string = [string]

    typer = len(string)

    valører = []
    multi = []
    antTerninger = []
    terningtyper = []
    totalListe = []

    for valør in range(0, typer):
        valører.append(string[valør].split(":")[0])  # KP
        rest = string[valør].split(":")[1]  # 4d6x100

        multi.append(int(rest.split("x")[1]))  # 100
        rest = rest.split("x")[0]
        antTerninger.append(int(rest.split("d")[0]))  # 4
        terningtyper.append(int(rest.split("d")[1]))  # 6

        pengeMengde = rollDice(antTerninger[valør], terningtyper[valør], multi[valør])
        totalListe.append(valører[valør] + str(pengeMengde))

    svarStreng = ""
    for e in range(len(totalListe)):
        string = str(string)
        svarStreng = svarStreng + totalListe[e]
        if len(totalListe) - e == 1:
            pass
        elif len(totalListe) - e == 2:
            svarStreng = svarStreng + " og "
        else:
            svarStreng = svarStreng + ", "
    return svarStreng


def equationSeparatorMagic(string):
    # string =  1d6;C, 1d4A,1d6B eller ""
    if string is None:
        return "ingen magiske gjenstander"

    if "," in string:
        string = string.split(",")
    else:
        string = [string]

    typer = len(string)

    typeItems = []
    antTerninger = []
    typeTerning = []
    totalListe = []

    for type in range(typer):
        typeItems.append(string[type].split(";")[1])  # A
        rest = string[type].split(";")[0]  # 1d6

        antTerninger.append(int(rest.split("d")[0]))  # 1
        typeTerning.append(int(rest.split("d")[1]))  # 6

        totalListe.append(
            str(rollDice(antTerninger[type], typeTerning[type], 1)) + f" gjenstander fra liste {typeItems}.")

    svarStreng = ""
    for e in range(len(totalListe)):
        svarStreng = svarStreng + totalListe[e]
        if len(totalListe) - e == 1:
            pass
        elif len(totalListe) - e == 2:
            svarStreng = svarStreng + " og "
        else:
            svarStreng = svarStreng + ", "

    return svarStreng


def lootRoll(cr, treasureRoll):
    lootCRDict = {
        range(0, 5): 1,
        range(5, 11): 3,
        range(11, 17): 5,
        range(17, sys.maxsize): 7
    }
    columnForCR = rangeIter(lootCRDict, cr)

    lootDice = findCell(columnForCR, treasureRoll, 5)
    svarListe = equationSeparatorCash(lootDice)
    return svarListe


def hoardRoll(cr, treasureRoll):
    hoardDiceDict = {
        range(0, 5): 9,
        range(5, 11): 12,
        range(11, 17): 15,
        range(17, sys.maxsize): 18
    }
    columnForCR = rangeIter(hoardDiceDict, cr)

    hoardDiceCash = findCellHoard(columnForCR, treasureRoll)
    hoardCashString = equationSeparatorCash(hoardDiceCash)  # string

    hoardDiceObjects = findCellHoard(columnForCR, treasureRoll)  # 2d6x10gp
    hoardObjectString = equationSeparatorCash(hoardDiceObjects)  # string

    objectType = findCellHoard(columnForCR + 1, treasureRoll)  # string

    hoardDiceMagic = findCellHoard(columnForCR + 2, treasureRoll)
    hoardMagicString = equationSeparatorMagic(hoardDiceMagic)  # string

    svarStreng = f"{hoardCashString}\n{hoardObjectString} {objectType}\n{hoardMagicString}"

    return svarStreng


def rangeIter(iterable, value):
    for element in iterable:
        if value in element:
            return iterable[element]
    print(f"Value out of range: rangeIter. Value: {value}")
    exit(2)
