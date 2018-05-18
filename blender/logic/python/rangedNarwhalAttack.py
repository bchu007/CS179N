import bge
import mathutils

velocity = 50

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
horn = cont.owner
player = scene.objects["2Ply"]

projectile = scene.addObject("ConeProjectile", horn, 60)
distance, globalvec, localvec = projectile.getVectTo(player)
projectile.alignAxisToVect(globalvec, 2)
globalvec.normalize()
projectile.setLinearVelocity(globalvec*velocity)

# Stall the narwhal
narwhal = horn.parent
narwhal["Count"] = 0
narwhal["Stall"] = True
narwhal.setLinearVelocity([0,0,0])
