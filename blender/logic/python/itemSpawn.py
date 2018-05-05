import bge
import random

def moveItem(i):
    i.position = [random.randint(-20, 20), random.randint(-20, 20), 20]
    print(i.position)
return

scene = bge.logic.getCurrentScene()

m16 = scene.addObject("m16", "ItemSpawner")
moveItem(m16)
m16_1 = scene.addObject("m16.001", "ItemSpawner")
moveItem(m16_1)

for object in scene.objects:
    print(object.name)
