import bge
import time
import itemSpawn

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
player = scene.objects["2Ply"]

def dropItem(obj):
    playerObj = "player" + obj
    scene = bge.logic.getCurrentScene()
    scene.objects[playerObj].visible = False
    scene.objects["2Ply"]["Item"] = ""
    dropObj = scene.addObject(obj, "m16Flare")
    dropObj.localLinearVelocity = [0,8,5]
    if (obj != "Egg"):
        dropObj["Ammo"] = scene.objects[playerObj]["Ammo"]
        scene.objects[playerObj]["Ammo"] = 0
        
    return dropObj

start = time.perf_counter()

if (cont.sensors["Mouse"].positive and cont.sensors["Keyboard"].positive and (player["PickupCooldown"] == 0)):    
    playerM16 = scene.objects["playerm16"]
    playerRocketLauncher = scene.objects["playerRocketLauncher"]
    playerEgg = scene.objects["playerEgg"]

    obj = bge.logic.getCurrentController().owner

    ## check if item is close enough
    distance, globalvec, localvec = obj.getVectTo(player);
    if distance < 10:
        print("INFO: Picking up " + obj.name)
        player["PickupCooldown"] = 10
        if (obj.name == "Egg"):
            ## check if player already has item
            if player["HasItem"] and player["Item"] != "Egg":
                dropItem(player["Item"])
            
            ## set player egg to visible
            if player["Item"] != "Egg":
                player["Item"] = "Egg"
                playerEgg.visible = True
                player["HasItem"] = True;
            else: ## Player is already holding the Egg
                print("ERROR: There shouldd't be multiple eggs")
            obj.endObject()
        ## Picking up M16
        elif (obj.name == "m16"): 
            ## check if player already has item
            if player["HasItem"] and player["Item"] != "m16":
                dropItem(player["Item"])  

            ## set player m16 to visible
            if player["Item"] != "m16":
                player["Item"] = "m16"
                playerM16.visible = True
                playerM16["Ammo"] = obj["Ammo"]
                player["HasItem"] = True;
            else: ## Player is already holding the m16 so add ammo
                playerM16["Ammo"] += obj["Ammo"]
                itemSpawn.spawnGun("m16")
            obj.endObject()
        ## Picking up health
        elif (obj.name == "HealthPack"):
            if (player["Health"] < 10):
                player["Health"] = 10
                obj.endObject()
        ## Picking up Rocket Launcher
        elif (obj.name == "RocketLauncher"): 
            ## check if player already has item
            if player["HasItem"] and player["Item"] != "RocketLauncher":
                dropItem(player["Item"])  

            ## set player m16 to visible
            if player["Item"] != "RocketLauncher":
                player["Item"] = "RocketLauncher"
                playerRocketLauncher.visible = True
                playerRocketLauncher["Ammo"] = obj["Ammo"]
                player["HasItem"] = True;
            else: ## Player is already holding the m16 so add ammo
                playerRocketLauncher["Ammo"] += obj["Ammo"]
                itemSpawn.spawnGun("RocketLauncher")
            obj.endObject()
                

end = time.perf_counter()
print("Performance Log: Pickup Item: " + str(end-start))