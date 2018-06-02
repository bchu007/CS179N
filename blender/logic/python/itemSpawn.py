import bge
import random
import time
import math

# Moves an item to random location on x and y
# and to the z location on the ground
def moveItemRandToGround(obj):
    # Assumption: The ground is below the object  
    radius = 125
    degrees = random.randint(0, 360)
    radians = math.radians(degrees)
    valuex = math.fabs(math.ceil(math.sin(radians)*radius))
    valuey = math.fabs(math.ceil(math.cos(radians)*radius))
    
    obj.worldPosition = [random.randint(-valuex, valuex), random.randint(-valuey, valuey), 100]
    colobj, point, normal = obj.rayCast([obj.position[0], obj.position[1], -100], None, 200)
    while (colobj is None or colobj.name != "Grid"):
        obj.worldPosition = [random.randint(-valuex, valuex), random.randint(-valuey, valuey), 100]
        colobj, point, normal = obj.rayCast([obj.position[0], obj.position[1], -100], None, 200)

    obj.worldPosition[2] = point[2] + 2

def moveItemToGround(obj):
    colobj, point, normal = obj.rayCast([obj.position[0], obj.position[1], -100], None, 200)
    obj.worldPosition[2] = point[2] + 2

def spawnGun(obj):
    print("INFO: Spawning " + obj)
    scene = bge.logic.getCurrentScene()
    createdObj = scene.addObject(obj, "ItemSpawner")
    moveItemRandToGround(createdObj)
    createdObj.suspendDynamics()


