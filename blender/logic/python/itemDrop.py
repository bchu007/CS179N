import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()

print("test")
if (cont.sensors["Drop"].positive and cont.sensors["HasItem"].positive):
    print("Dropping Item")
    playerM16 = scene.objects["playerM16"]
    player = scene.objects["2Ply"]
    
    player["HasItem"] = False
    if (player["Item"] == "playerM16"):
        playerM16.visible = False
        player["Item"] = ""
        dropObj = scene.addObject("m16", "2Ply")
        dropObj.localLinearVelocity = [0,-8,5]