import bge
import time

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
if (cont.sensors["Mouse"].positive and cont.sensors["Keyboard"].positive):
    start = time.perf_counter()
    
    playerM16 = scene.objects["playerM16"]
    player = scene.objects["2Ply"]

    obj = bge.logic.getCurrentController().owner

    ## check if gun is close enough
    distance, globalvec, localvec = obj.getVectTo(player);
    if distance < 10:
        print(obj.name)
        ## Picking up M16
        if (obj.name == "m16"): 
            ## check if player already has item
            if player["HasItem"] and not(player["Item"] == "playerM16"):
                print("TODO")        
                ## TODO Drop the current item      
            
            ## Pick up the M16
            player["HasItem"] = True;
            ## set player m16 to visible
            if not player["Item"] == "playerM16":
                player["Item"] = "playerM16"
                playerM16.visible = True
                ## TODO make other models invisible
            else: ## Player is already holding the m16 so add ammo
                print("TODO")
                ## TODO
                    
            obj.endObject()

    end = time.perf_counter()
    print("Performance Log: Pickup Item: " + str(end-start))