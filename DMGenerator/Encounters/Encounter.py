## Generer et spesifikt encounter
# Importer moduler
import random


# Angi variable for operasjonen

def expMulti(monsterQuant):
    # Encounter Multiplier (DMG s.82)
    monsterQuant = int(monsterQuant)
    if monsterQuant == 1:
        return 1
    elif monsterQuant == 2:
        return 1.5
    elif monsterQuant in range(3, 7):
        return 2
    elif monsterQuant in range(7, 11):
        return 2.5
    elif monsterQuant in range(11, 15):
        return 3
    elif monsterQuant >= 15:
        return 4
    elif monsterQuant < 1:
        return 0
    else:
        return "Uff da"


def encounter(maxExp, valids, valids_cr):
    validMonsters = valids
    validMonsters_cr = valids_cr
    expList = {0: 10,  # CR 0
               1: 25,  # CR 1/8
               2: 50,  # CR 1/4
               3: 100,  # CR 1/2
               4: 200,  # CR 1
               5: 450,  # CR 2
               6: 700,  # CR 3
               7: 1100,  # CR 4
               8: 1800,  # CR 5
               9: 2300,  # CR 6
               10: 2900,  # CR 7
               11: 3900,  # CR 8
               12: 5000,  # CR 9
               13: 5900,  # CR 10
               14: 7200,  # CR 11
               15: 8400,  # CR 12
               16: 10000,  # CR 13
               17: 11500,  # CR 14
               18: 13000,  # CR 15
               19: 15000,  # CR 16
               20: 18000,  # CR 17
               21: 20000,  # CR 18
               22: 22000,  # CR 19
               23: 25000,  # CR 20
               24: 33000,  # CR 21
               25: 41000,  # CR 22
               26: 50000,  # CR 23
               27: 62000,  # CR 24
               28: 75000,  # CR 25
               29: 90000,  # CR 26
               30: 105000,  # CR 27
               31: 120000,  # CR 28
               32: 135000,  # CR 29
               33: 155000  # CR 30
               }
    crList = {0: 0,
              1: 1 / 8,
              2: 1 / 4,
              3: 1 / 2,
              4: 1,
              5: 2,
              6: 3,
              7: 4,
              8: 5,
              9: 6,
              10: 7,
              11: 8,
              12: 9,
              13: 10,
              14: 11,
              15: 12,
              16: 13,
              17: 14,
              18: 15,
              19: 16,
              20: 17,
              21: 18,
              22: 19,
              23: 20,
              24: 21,
              25: 22,
              26: 23,
              27: 24,
              28: 25,
              29: 26,
              30: 27,
              31: 28,
              32: 29,
              33: 30
              }

    encounterList = []
    encounterList_number = []
    sumExp = 0

    # Fyll en liste med monstre som passer kvalifikasjonene
    def pickAnEnemy(totalExp):
        pickAMonster = random.randrange(len(validMonsters) - 1)
        pickedMonster = validMonsters[pickAMonster]
        expFromMonster = expList[int(validMonsters_cr[pickAMonster])]
        encounterList.append(pickedMonster)
        encounterList_number.append(1)

        while totalExp * expMulti(sum(encounterList_number)) < maxExp:
            potentialExp = int((totalExp + expFromMonster) * expMulti(sum(encounterList_number) + 1))

            if potentialExp > maxExp:
                break
            else:
                encounterList_number[encounterList.index(pickedMonster)] += 1
                totalExp += expFromMonster
        return totalExp

    sumExp = pickAnEnemy(sumExp)
    while (sumExp * expMulti(sum(encounterList_number))) * 100 / maxExp < 10:
        sumExp += pickAnEnemy(sumExp)

    encounter = zip(encounterList_number, encounterList)
    encounter = list(encounter)

    #print("Encounter list: ", encounterList)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n-------------------------------------")
    print("Dette er encounteret:\n" + "\n".join([str(i) for i in encounter]))
    print("Experience", sumExp)
    print("Difficulty: ", sumExp * expMulti(sum(encounterList_number)))
