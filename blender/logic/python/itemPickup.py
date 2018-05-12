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
        ## check if player already has item
        if player["HasItem"] and not(player["Item"] == "playerM16"):        
            print("Player already has Item that is not the M16")
            ## TODO Drop the current item      
        
        ## Pick up the M16
        player["HasItem"] = True;
        ## set player m16 to visible
        if not player["Item"] == "playerM16":
            player["Item"] = "playerM16"
            playerM16.visible = True
            ## TODO make other models invisible
        else: ## Player is already holding the m16 so add ammo
            ## TODO
            print("Adding Ammo")
                
        obj.endObject()
