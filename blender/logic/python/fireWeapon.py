import bge
import time
import itemSpawn

start = time.perf_counter()

scene = bge.logic.getCurrentScene()
player = scene.objects["2Ply"]
flare = scene.objects["m16Flare"]
render = bge.render
camera = scene.active_camera

player.color = [1, 0, 0, 1]

if player["Item"] == "m16":
    ## Dec Ammo
    playerM16 = scene.objects["playerm16"]
    if (playerM16["Ammo"] > 0):
        playerM16["Ammo"] -= 1
        
        ## Draw Vec
        fromVec = flare.worldPosition
        toVec = camera.position - camera.getScreenVect(0.5, 0.5) * 50
        
        color = [0.9, 0.9, 0.8]
        
        hitobj, point, normal = camera.rayCast(toVec, camera.worldPosition, 200)
        ## Calc hit damage
        if (hitobj != None and hitobj.getPropertyNames().count("health") != 0):
            toVec = point
            hitobj["health"] -= 1
            
        render.drawLine(fromVec, toVec, color)
    else:
        itemSpawn.spawnGun("m16")
        playerM16.visible = False
        player["Item"] = ""
        player["HasItem"] = False
        flare.visible = False
    
end = time.perf_counter()
print("Performance Log: Fire weapon: " + str(end-start))