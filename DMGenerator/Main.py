from Encounters.create_encounter import createEncounter
from DungeonGenerator.chamber import chamber
from DungeonGenerator.door import door
from DungeonGenerator.passage import passage
from DungeonGenerator.room_descriptor import roomDescript
from DungeonGenerator.stairs import stairs
from DungeonGenerator.start import start
from DungeonGenerator.trap import trap
from Treasure.TreasureGenerator import treasure
from defs import *


#dungeonType = input("Hvilken type Dungeoun skal beskrivelsene tas fra?")
dungeonType = "y"
lastValueCalled = ""

while 1 == 1:
    #if lastValueCalled in ["chamber", "encounter", "treasure"]:
    #    waitForEnter = input("Trykk på enter for å fortsette")
    print("""
\'start\'       :   startsted.
\'ecounter\'    :   setter i gang encounter.
\'passage\'     :   korridor.
\'chamber\'     :   rom.
\'describe\'    :   beskrivelse av rommet.
\'door\'        :   door.
\'stairs\'      :   trapper.
\'trap\',
\'trick\',
\'hazard\',
\'obstacle\'    :   velg hvilken hindring du vil ha
\'treasure\'    : skatt (loot eller hoard).""")
    print("Skriv inn koden for kommandoen du vil bruke")
    prompt = input("")
    if prompt in {"0", "q", ""}:
        break
    else:
        # print(prompt)
        print("-----------------------")
        if prompt == "start":
            lastValueCalled = "start"
            start()
        elif prompt == "encounter":
            lastValueCalled = "encounter"
            createEncounter()
        elif prompt == "passage":
            lastValueCalled = "passage"
            passage()
        elif prompt == "chamber":
            lastValueCalled = "chamber"
            chamber()
        elif prompt == "describe":
            lastValueCalled = "describe"
            roomDescript(dungeonType)
        elif prompt == "door":
            lastValueCalled = "door"
            door()
        elif prompt == "stairs":
            lastValueCalled = "stairs"
            stairs()
        elif prompt == "trap" or prompt == "trick" or prompt == "hazard" or prompt == "obstacle":
            lastValueCalled = "traps"
            #type = input("Skriv trap, trick, hazard eller obstacle. ")
            trap(prompt)
        elif prompt == "treasure":
            lastValueCalled = "treasure"
            type = input("Skriv \"loot\" eller \"hoard\" ")
            cr = inTput("Skriv inn en CR for fienden som eier dette. ")
            treasure(type, cr)
        print("-----------------------")
