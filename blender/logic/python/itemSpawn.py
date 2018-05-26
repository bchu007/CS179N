import bge
import random
import time

# Moves an item to random location on x and y
# and to the z location on the ground
def moveItemRandToGround(obj):
    # Assumption: The ground is below the object  
    obj.worldPosition = [random.randint(-100, 100), random.randint(-100, 100), 100]
    colobj, point, normal = obj.rayCast([obj.position[0], obj.position[1], -100], None, 200)
    while (colobj is None or colobj.name != "Grid"):
        obj.worldPosition = [random.randint(-100, 100), random.randint(-100, 100), 100]
        colobj, point, normal = obj.rayCast([obj.position[0], obj.position[1], -100], None, 200)

    obj.worldPosition[2] = point[2] + 2

def moveItemToGround(obj):
    colobj, point, normal = obj.rayCast([obj.position[0], obj.position[1], -100], None, 200)
    obj.worldPosition[2] = point[2] + 1

def spawnGun(obj):
    print("INFO: Spawning " + obj)
    scene = bge.logic.getCurrentScene()
    createdObj = scene.addObject(obj, "ItemSpawner")
    moveItemRandToGround(createdObj)
    createdObj.suspendDynamics()


