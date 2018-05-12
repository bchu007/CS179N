import bge

scene = bge.logic.getCurrentScene()
player = scene.objects["2Ply"]
flare = scene.objects["m16Flare"]
render = bge.render
camera = scene.active_camera

if player["Item"] == "playerM16":
    print("Fire M16")
    fromVec = flare.worldPosition
    toVec = camera.position - camera.getScreenVect(0.5, 0.5) * 50
    print(toVec)
    
    color = [0.9, 0.9, 0.8]
    render.drawLine(fromVec, toVec, color)