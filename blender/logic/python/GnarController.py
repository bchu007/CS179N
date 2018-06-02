import bge
import random
import mathutils

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
render = bge.render
gnar = cont.owner
player = scene.objects['2Ply']
Laser = "Laser"

toVec = player.worldPosition

hit = gnar.rayCastTo(toVec)

if (gnar["gtimer"] == 0 and gnar['trigger'] == 1):
    numLasers = random.randint(1, 3)
    for i in range(0, numLasers):
        laser = scene.addObject(Laser, player)
        xRand = random.randint(-7, 7)
        yRand = random.randint(-7, 7)
        laser.worldPosition = player.worldPosition
        laser.worldPosition.x += xRand
        laser.worldPosition.y += yRand
        laser['trigger'] = 1