import bge
import random
import time

start = time.perf_counter()

scene = bge.logic.getCurrentScene()
ground = scene.objects["Grid"]

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



print("Spawning M16s")

m16 = []
for i in range(10):
    name = "m16"
    m16.append(scene.addObject(name, "ItemSpawner"))
    moveItemRandToGround(m16[i])
    m16[i].suspendDynamics()
    
print("Done Spawning M16s")

end = time.perf_counter()
print("Performance Log: Spawn Items and Enemies: " + str(end-start))



