import bge
import itemSpawn

scene = bge.logic.getCurrentScene()
owner = bge.logic.getCurrentController().owner

int = owner["GameTime"]
wave = owner["Wave"]

## Check for wave end
def WaveEnd():
    for obj in scene.objects:
        if (obj.name == "NarwhalArmature"):
            return False
        
    owner["Wave"] += 1
    owner["GameTime"] = 0
    return True

if (wave == 1):
    if (int == 0):
        ## Spawn Egg and guns
        ## Egg
        egg = scene.addObject("Egg", "ItemSpawner")
        itemSpawn.moveItemToGround(egg)
        ## Guns
        for i in range(10):
            obj = itemSpawn.spawnGun("m16")
            obj.suspendDynamics()
            obj = itemSpawn.spawnGun("RocketLauncher")
            obj.suspendDynamics()
            obj = itemSpawn.spawnGun("Shotgun")
            obj.suspendDynamics()
        ## Health Pack
        for i in range(5):
            itemSpawn.spawnGun("HealthPack")
    if (int == 10):
        print("INFO: Wave 1 start")
        
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner3", "")
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
    elif(int == 40):
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner11", "")
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
        WaveEnd()
        
        print("TODO: Check for narwhals fallen off the map")
        
elif (wave == 2):
    if (int == 10):
        print("INFO : Wave 2 start")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner11", "")
    elif (int == 30):
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
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner12", "")
    elif(int >= 71):
        WaveEnd()
        
        print("TODO: Check for narwhals fallen off the map")
        
elif (wave == 3):
    if (int == 10):
        print("INFO: Wave 3 start")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "c2", "NarwhalSpawner11", "")
    elif (int == 30):
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner11", "")
    elif(int == 60):
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "c1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "c2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "c2", "NarwhalSpawner12", "")

    elif(int >= 71):
        WaveEnd()
        
        print("TODO: Check for narwhals fallen off the map")
        
elif (wave == 4):
    if (int == 10):
        print("INFO: Wave 4 start")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner11", "")
    elif (int == 30):
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner1", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner5", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner7", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner11", "")
    elif(int == 50):
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "c2", "NarwhalSpawner4", "")
        bge.logic.sendMessage("Spawn", "r2", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "c2", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner10", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner12", "")
        bge.logic.sendMessage("Spawn", "c2", "NarwhalSpawner2", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner8", "")
        bge.logic.sendMessage("Spawn", "n2", "NarwhalSpawner12", "")

    elif(int >= 71):
        WaveEnd()
        
        print("TODO: Check for narwhals fallen off the map")
        
elif (wave == 5):
    if (int == 10):
        print("INFO: Wave 5 start")
        ## Spawn Gnar
        print("INFO: Spawning Gnar!")
        scene.addObject("Gnar", "ItemSpawner")
    elif((int-10) % 30 == 0):
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner1", "")
        
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner3", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner4", "")
        
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner6", "")
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner7", "")
        
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner9", "")
        bge.logic.sendMessage("Spawn", "n1", "NarwhalSpawner10", "")
        
        bge.logic.sendMessage("Spawn", "r1", "NarwhalSpawner12", "")
    elif(int >= 11):
        ## Check if Gnar is dead
        if (scene.objects["Gnar"]["health"] <= 0):
            print("INFO: Game win")
            owner["Wave"] += 1
        
        print("TODO: Check for narwhals fallen off the map")
        