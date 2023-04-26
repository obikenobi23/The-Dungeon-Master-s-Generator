from start import start
from door import door
from passage import passage
from chamber import chamber
from stairs import stairs
from room_descriptor import roomDescript
from trap import trap
#fromm treasure import treasure

#dungeonType = input("Hvilken type Dungeoun skal beskrivelsene tas fra?")
dungeonType = "y"

while 1 == 1:
    prompt = input("")
    if prompt == "0":
        break
    else:
        if prompt == "start":
            start()
        elif prompt == "passage":
            passage()
        elif prompt == "chamber":
            chamber()
        elif prompt == "descibe":
            roomDescript(dungeonType)
        elif prompt == "door":
            door()
        elif prompt == "stairs":
            stairs()
        elif prompt == "trap" or prompt == "trick" or prompt == "hazard" or prompt == "obstacle":
            #type = input("Skriv trap, trick, hazard eller obstacle. ")
            trap(prompt)
        elif prompt == "describe":
            roomDescript()
        #elif prompt == "treasure":
            #treasure()