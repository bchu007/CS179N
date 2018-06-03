import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
player = scene.objects["2Ply"]

obj = scene.addObject("RocketExplosion", cont.owner, 80)
child = obj.children["Explosion1"]
child.visible = False
obj.actuators["Sound"].startSound()

print(cont.owner.sensors["Collision"].hitObject)