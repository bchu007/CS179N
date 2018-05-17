import bge
import time

start = time.perf_counter()

scene = bge.logic.getCurrentScene()
player = scene.objects["2Ply"]
flare = scene.objects["m16Flare"]
render = bge.render
camera = scene.active_camera

player.color = [1, 0, 0, 1]

if player["Item"] == "playerM16":
    fromVec = flare.worldPosition
    toVec = camera.position - camera.getScreenVect(0.5, 0.5) * 50
    
    color = [0.9, 0.9, 0.8]
    render.drawLine(fromVec, toVec, color)
    
    hitobj = camera.rayCastTo(toVec,200)
    if (hitobj != None and hitobj.getPropertyNames().count("health") != 0):
        hitobj["health"] -= 1
    
end = time.perf_counter()
print("Performance Log: Fire weapon: " + str(end-start))