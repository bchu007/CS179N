import bge
import random
import mathutils

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
spawner = cont.owner

# Moves the narwhal to random position +-8 away from spawner
def moveObjRandToGround(obj):
    # Assumption: The ground is below the object 
    randDistance = 1
    pos = obj.worldPosition
    pos += mathutils.Vector((random.randint(-randDistance, randDistance), random.randint(-randDistance, randDistance), 0))
    pos[2] = 90
    colobj, point, normal = obj.rayCast([pos[0], pos[1], -100], None, 200)
    
    # If the narwhal didn't collide with the grid then re randomize its position
    # Increase the random distance it can spawn from spawner in case its getting stuck on other spawned narwhals
    # !!!! Problem: Increases Likelhood of spawning off map
    # !!!! Solution: Bound values to map boundries
    while (colobj is None or colobj.name != "Grid"):
        pos = obj.worldPosition
        pos += mathutils.Vector((random.randint(-randDistance, randDistance), random.randint(-randDistance, randDistance), 0))
        pos[2] = 90
        colobj, point, normal = obj.rayCast([pos[0], pos[1], -100], None, 200)
        randDistance += 1
        if (colobj is not None):
            print(colobj.name)
        if (randDistance >= 30):
            print("ERROR: Aborting Spawning at: " + spawner.name)
            obj.endObject()
            return
    
    obj.worldPosition = pos
    obj.worldPosition[2] = point[2] + 3

## Start
message = cont.sensors["Spawn"]
list = message.bodies

for m in list:
    narwhalToSpawn = ""
    ## m[0] char - (n)ormal, (r)anged, (c)harge
    ## m[1] int - number to spawn
    if m[0] == 'n':
        narwhalToSpawn = "NarwhalArmature"
    elif m[0] == 'r':
        narwhalToSpawn = "NarwhalRangedArmature"
    elif m[0] == 'c':
        narwhalToSpawn = "NarwhalChargeArmature"
        
    for i in range(0, int(m[1])):
        obj = scene.addObject(narwhalToSpawn, spawner)
        moveObjRandToGround(obj)
    