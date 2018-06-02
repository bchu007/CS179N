import bge
import mathutils

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
laser = cont.owner

if laser['trigger'] == 1:
    cont.activate('Grow')
    laser['trigger'] = 2