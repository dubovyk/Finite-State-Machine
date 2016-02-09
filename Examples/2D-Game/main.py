from fsm import *
import cocos
import pyglet
from pyglet.window import key

width = 700
height = 700


class RotatingText(cocos.text.Label):

    def __init__(self, text='', pos=(0, 0)):
        super(RotatingText, self).__init__(text=text, position=pos, font_size=32)
        self.schedule(self.update)

    def update(self, dt):
        self.rotation += 60 * dt


class KeyboardControlledObject(cocos.actions.Move):

    def step(self, dt):
        super(KeyboardControlledObject, self).step(dt)

        velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
        velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])
        self.target.velocity = (velocity_x, velocity_y)


def main():
    global keyboard
    cocos.director.director.init(width=700, height=700)

    player_layer = cocos.layer.Layer()
    me = cocos.sprite.Sprite('img.png')
    me.scale = 0.512
    text = RotatingText('Hi guys!', (500, 500))
    # Set initial position and velocity.
    me.position = (200, 100)
    me.velocity = (0, 0)
    # Set the sprite's movement class.
    me.do(KeyboardControlledObject())
    player_layer.add(me)
    player_layer.add(text)
    # Create a scene and set its initial layer.
    main_scene = cocos.scene.Scene(player_layer)
    # Attach a KeyStateHandler to the keyboard object.
    keyboard = key.KeyStateHandler()
    cocos.director.director.window.push_handlers(keyboard)
    # Play the scene in the window.
    cocos.director.director.run(main_scene)

main()
