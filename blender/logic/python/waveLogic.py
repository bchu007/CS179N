import bge
import itemSpawn

scene = bge.logic.getCurrentScene()
owner = bge.logic.getCurrentController().owner

int = owner["GameTime"]
wave = owner["Wave"]

if (wave == 1):
    if (int == 0):
        ## Spawn Egg and guns
        ## Egg
        egg = scene.addObject("Egg", "ItemSpawner")
        itemSpawn.moveItemToGround(egg)
        egg.suspendDynamics()
        ## Guns
        for i in range(20):
            itemSpawn.spawnGun("m16")
            itemSpawn.spawnGun("RocketLauncher")
            itemSpawn.spawnGun("Shotgun")
        ## Health Pack
        for i in range(5):
            itemSpawn.spawnGun("HealthPack")
    if (int == 10):
        print("Wave 1 start")
        
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner11", "")
    elif (int == 20):
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner12", "")
    elif(int == 50):
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner10", "")
    elif(int == 70):
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner11", "")
    elif(int >= 71):
        ## Check for wave end
        waveEnd = True
        for obj in scene.objects:
            if (obj.name == "NarwhalArmature"):
                waveEnd = False
        
        if (waveEnd == True):
            owner["Wave"] += 1
            owner["GameTime"] = 0
        
        print("TODO: Check for narwhals fallen off the map")
        
elif (wave == 2):
    if (int == 10):
        print("Wave 2 start")
        print("TODO: Spawn Guns")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner11", "")
    elif (int == 20):
        bge.logic.sendMessage("Spawn", "r3", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n3", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner12", "")
    elif (int == 40):
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner11", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner11", "")
    elif(int == 70):
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner12", "")
    elif(int >= 71):
        ## Check for wave end
        waveEnd = True
        for obj in scene.objects:
            if (obj.name == "NarwhalArmature"):
                waveEnd = False
        
        if (waveEnd == True):
            owner["Wave"] += 1
            owner["GameTime"] = 0
        
        print("TODO: Check for narwhals fallen off the map")