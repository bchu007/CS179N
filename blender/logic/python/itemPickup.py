import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
if (cont.sensors["Mouse"].positive and cont.sensors["Keyboard"].positive):
    playerM16 = scene.objects["playerM16"]
    player = scene.objects["2Ply"]

    obj = bge.logic.getCurrentController().owner

    ## check if gun is close enough
    distance, globalvec, localvec = obj.getVectTo(player);
    print(distance)
    if distance < 10:
        ## set player m16 to visible
        if playerM16.visible == False:
            playerM16.visible = True
        else:
            ## TODO
            print("Adding Ammo")
            
        obj.endObject()
