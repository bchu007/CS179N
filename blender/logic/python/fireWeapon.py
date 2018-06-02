import bge
import time
import itemSpawn
import random
import mathutils

start = time.perf_counter()

controller = bge.logic.getCurrentController()
status = controller.sensors["Fire"].getButtonStatus(bge.events.LEFTMOUSE)

if status == bge.logic.KX_INPUT_JUST_ACTIVATED or status == bge.logic.KX_INPUT_ACTIVE:
    scene = bge.logic.getCurrentScene()
    player = scene.objects["2Ply"]
    flare = scene.objects["m16Flare"]
    render = bge.render
    camera = scene.active_camera
    rocketVelocity = 100        
    m16Damage = 1
    shotgunDamage = 0.2
    shotgunRange = 100
    shotgunPellets = 30
    shotgunSpread = 5
    color = [1, 0.8, 0.5]

    if ((player["Item"] == "m16") and (player["M16Cooldown"] == 0)):
        ## Check Ammo
        playerM16 = scene.objects["playerm16"]
        if (playerM16["Ammo"] > 0):
            playerM16["Ammo"] -= 1
            player["M16Cooldown"] = 15
            
            ## Draw Vec
            fromVec = flare.worldPosition
            toVec = camera.worldPosition - (camera.getScreenVect(0.5, 0.5) * 50)
            
            ## Play Sound
            playerM16.actuators["Sound"].stopSound()
            playerM16.actuators["Sound"].startSound()
            
            hitobj, point, normal = camera.rayCast(toVec, camera.worldPosition, 200, "Enemy", 0, 1)
            ## Calc hit damage
            if (hitobj != None and hitobj.getPropertyNames().count("health") != 0):
                toVec = point
                hitobj["health"] -= m16Damage
                print("INFO: Hit " + hitobj.name + " with rifle")
                if ("DamageSound" in hitobj.actuators):
                    hitobj.actuators["DamageSound"].stopSound()
                    hitobj.actuators["DamageSound"].startSound()
                
            render.drawLine(fromVec, toVec, color)
        ## Get rid of gun if ammo is now 0
        if (playerM16["Ammo"] == 0):
            itemSpawn.spawnGun("m16")
            playerM16.visible = False
            player["Item"] = ""
            player["HasItem"] = False
            flare.visible = False
            
    elif player["Item"] == "RocketLauncher" and player["RocketCooldown"] == 0:
        ## Check Ammo
        playerRocketLauncher = scene.objects["playerRocketLauncher"]
        if playerRocketLauncher["Ammo"] > 0:
            playerRocketLauncher["Ammo"] -= 1
            player["RocketCooldown"] = 60
            
            ## Play Sound
            playerRocketLauncher.actuators["Sound"].stopSound()
            playerRocketLauncher.actuators["Sound"].startSound()
            
            rocket = scene.addObject("Rocket", "playerRocketLauncherTip", 60)
            toVec = -(camera.getScreenVect(0.5, 0.5) * 50)
            rocket.alignAxisToVect(toVec, 0)
            toVec.normalize()
            rocket.setLinearVelocity(toVec*rocketVelocity)
        ## Get rid of gun if ammo is now 0
        if (playerRocketLauncher["Ammo"] == 0):
            itemSpawn.spawnGun("RocketLauncher")
            playerRocketLauncher.visible = False
            player["Item"] = ""
            player["HasItem"] = False
            
    elif ((player["Item"] == "Shotgun") and (player["ShotgunCooldown"] == 0)):
        ## Check Ammo
        playerShotgun = scene.objects["playerShotgun"]
        if (playerShotgun["Ammo"] > 0):
            playerShotgun["Ammo"] -= 1
            player["ShotgunCooldown"] = 30
            
            ## Get vec to center screen
            toVec = camera.worldPosition - (camera.getScreenVect(0.5, 0.5) * shotgunRange)
            ## Play Sound
            playerShotgun.actuators["Sound"].stopSound()
            playerShotgun.actuators["Sound"].startSound()
            
            ## Fire pellets
            for i in range(shotgunPellets):
                rand = mathutils.Vector((random.randrange(-shotgunSpread, shotgunSpread, 1), random.randrange(-shotgunSpread, shotgunSpread, 1), random.randrange(-shotgunSpread, shotgunSpread, 1)))
                vec = toVec + rand
                
                ## Draw Vec
                fromVec = flare.worldPosition
                render.drawLine(fromVec, vec, color)
                
                hitobj, point, normal = camera.rayCast(vec, camera.worldPosition, shotgunRange, "Enemy", 0, 1)
                ## Calc hit damage
                if (hitobj != None and hitobj.getPropertyNames().count("health") != 0):
                    hitobj["health"] -= shotgunDamage
                    print("INFO: Hit " + hitobj.name + " with shotgun")
                    if ("DamageSound" in hitobj.actuators):
                        hitobj.actuators["DamageSound"].stopSound()
                        hitobj.actuators["DamageSound"].startSound()
                
                
        ## Get rid of gun if ammo is now 0
        if (playerShotgun["Ammo"] == 0):
            itemSpawn.spawnGun("Shotgun")
            playerShotgun.visible = False
            player["Item"] = ""
            player["HasItem"] = False
        
    end = time.perf_counter()
    print("Performance Log: Fire weapon: " + str(end-start))