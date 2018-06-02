import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
player = scene.objects["2Ply"]

obj = scene.addObject("RocketExplosion", cont.owner, 45)
child = obj.children["Explosion1"]
child.visible = False
child.actuators["Sound"].startSound()