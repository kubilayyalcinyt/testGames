from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


game = Ursina()


level = Entity(model="level1_level.obj", texture="colorPalatte.png", collider="mesh", x=5, z=10)
img = Entity(model="level1_2_img.obj", texture="logo.png", collider="mesh", x=5, z=10)
lamb = Entity(model="level1_3_lamb.obj", color=color.white, collider="mesh", x=5, z=10) 
end = Entity(model="level1_end", color=color.red, collider="mesh", x=5, z=10) 

player = FirstPersonController(x=1, z=1, y=1, scale=2)

cube = Entity(model="cube", color=color.red, x=5, z=10, y=2)

def update():
    cube.rotation += Vec3(0,1,100)


















game.run()



#  ```py

# ```