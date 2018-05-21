import bge

scene = bge.logic.getCurrentScene()
owner = bge.logic.getCurrentController().owner

int = owner["GameTime"]
wave = owner["Wave"]

if (wave == 1):
    if (int == 10):
        print("Wave 1 start")
    elif (int == 15):
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
elif (wave == 2):
    if (int == 10):
        print("Wave 2 start")