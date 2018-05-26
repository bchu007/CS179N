import bge
import time
import mathutils

start = time.perf_counter()

scene = bge.logic.getCurrentScene()
player = scene.objects["2Ply"]
cont = bge.logic.getCurrentController()

def dropItem(obj):
    playerObj = "player" + obj
    scene = bge.logic.getCurrentScene()
    scene.objects[playerObj].visible = False
    scene.objects["2Ply"]["Item"] = ""
    dropObj = scene.addObject(obj, "2Ply")
    dropObj.localLinearVelocity = [0,-8,5]
    if (obj != "Egg"):
        dropObj["Ammo"] = scene.objects[playerObj]["Ammo"]
        scene.objects[playerObj]["Ammo"] = 0
        
    return dropObj

    
if (cont.sensors["Drop"].positive and cont.sensors["HasItem"].positive):
    player["HasItem"] = False
    
    if (player["Item"] == "Egg"):
        dropItem("Egg")
    elif (player["Item"] == "m16"):
        print("Drop M16")
        dropItem("m16")
        
end = time.perf_counter()
print("Performance Log: Drop Item: " + str(end-start))