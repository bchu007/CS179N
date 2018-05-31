import bge
import time
import itemSpawn
import mathutils

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
player = scene.objects["2Ply"]
camera = scene.active_camera

def dropItem(obj):
    playerObj = "player" + obj
    scene.objects[playerObj].visible = False
    scene.objects["2Ply"]["Item"] = ""
    dropObj = scene.addObject(obj, "m16Flare")
    worldV = -camera.getScreenVect(0.5, 0.5)
    worldV[2] = 0
    worldV.normalize()
    worldV *= 10
    localV = mathutils.Vector((0, 0, 5))
    if player.sensors["Forward"].positive:
        localV[1] += 5
    if player.sensors["Backward"].positive:
        localV[1] -= 4
    dropObj.localLinearVelocity += localV
    dropObj.worldLinearVelocity += worldV
    if (obj != "Egg"):
        dropObj["Ammo"] = scene.objects[playerObj]["Ammo"]
        scene.objects[playerObj]["Ammo"] = 0
    else:
        dropObj["Health"] = scene.objects[playerObj]["Health"]
        scene.objects[playerObj]["Health"] = 0
        
    return dropObj

start = time.perf_counter()

if (cont.sensors["Mouse"].positive and cont.sensors["Keyboard"].positive and (player["PickupCooldown"] == 0)):    
    playerM16 = scene.objects["playerm16"]
    playerRocketLauncher = scene.objects["playerRocketLauncher"]
    playerShotgun = scene.objects["playerShotgun"]
    playerEgg = scene.objects["playerEgg"]

    obj = cont.sensors["Mouse"].hitObject

    ## check if item is close enough
    distance, globalvec, localvec = obj.getVectTo(player);
    if distance < 10:
        print("INFO: Picking up " + obj.name)
        player["PickupCooldown"] = 15
        if (obj.name == "Egg"):
            ## check if player already has item
            if player["HasItem"] and player["Item"] != "Egg":
                dropItem(player["Item"])
            
            ## set player egg to visible
            if player["Item"] != "Egg":
                player["Item"] = "Egg"
                playerEgg.visible = True
                playerEgg["Health"] = obj["Health"]
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
        ## Picking up Shotgun
        elif (obj.name == "Shotgun"): 
            ## check if player already has item
            if player["HasItem"] and player["Item"] != "Shotgun":
                dropItem(player["Item"])  

            ## set player m16 to visible
            if player["Item"] != "Shotgun":
                player["Item"] = "Shotgun"
                playerShotgun.visible = True
                playerShotgun["Ammo"] = obj["Ammo"]
                player["HasItem"] = True;
            else: ## Player is already holding the m16 so add ammo
                playerShotgun["Ammo"] += obj["Ammo"]
                itemSpawn.spawnGun("Shotgun")
            obj.endObject()
                

        end = time.perf_counter()
        print("Performance Log: Pickup Item: " + str(end-start))