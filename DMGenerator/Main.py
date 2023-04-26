from Encounters.create_encounter import createEncounter
from DungeonGenerator.chamber import chamber
from DungeonGenerator.door import door
from DungeonGenerator.passage import passage
from DungeonGenerator.room_descriptor import roomDescript
from DungeonGenerator.stairs import stairs
from DungeonGenerator.start import start
from DungeonGenerator.trap import trap
from Treasure.TreasureGenerator import treasure

#dungeonType = input("Hvilken type Dungeoun skal beskrivelsene tas fra?")
dungeonType = "y"
lastValueCalled = ""

while 1 == 1:
    if lastValueCalled in ["chamber", "encounter", "treasure"]:
        waitForEnter = input("Trykk på enter for å fortsette")
    print("\'start\': startsted.\n\'ecounter\': setter i gang encounter.\n\'passage\': korridor.\n\'chamber\': rom.\n\'describe\': beskrivelse av rommet.\n\'door\': door.\n\'stairs\': trapper.\n\'trap\', \'trick\', \'hazard\', \'obstacle\'\n\'treasure\': skatt (loot eller hoard).")
    prompt = input("")
    if prompt == "0":
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
            cr = int(input("Skriv inn en CR for fienden som eier dette. "))
            treasure(type, cr)
        print("-----------------------")
