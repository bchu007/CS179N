import bge

controller = bge.logic.getCurrentController()
narwhal = controller.owner

narwhal.setLinearVelocity([0, narwhal["Knockback"], 0], True)
narwhal["Knockback"] = narwhal["Knockback"] - 1
print("Hit")