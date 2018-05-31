import bge
import time
import mathutils

start = time.perf_counter()

scene = bge.logic.getCurrentScene()
player = scene.objects["2Ply"]
cont = bge.logic.getCurrentController()
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
    
if (cont.sensors["Drop"].positive and cont.sensors["HasItem"].positive):
    player["HasItem"] = False
    
    if (player["Item"] == "Egg"):
        print("INFO: Drop Egg")
        dropItem("Egg")
    elif (player["Item"] == "m16"):
        print("INFO: Drop M16")
        dropItem("m16")
    elif (player["Item"] == "RocketLauncher"):
        print("INFO: Drop RocketLauncher")
        dropItem("RocketLauncher")
    elif (player["Item"] == "Shotgun"):
        print("INFO: Drop Shotgun")
        dropItem("Shotgun")
        
end = time.perf_counter()
print("Performance Log: Drop Item: " + str(end-start))