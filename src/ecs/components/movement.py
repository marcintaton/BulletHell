from panda3d.core import LVecBase3f
from src.ecs.component import Component


class Movement(Component):

    def __init__(self, parent):
        super().__init__(parent)
        self.movement_vector = LVecBase3f(0, 0, 0)
        self.rotation_vector = LVecBase3f(0, 0, 0)

    def set_movement(self, x, y, speed=1):
        self.movement_vector = LVecBase3f(x, 0, y).normalized() * speed

    def set_rotation(self, rot, speed=1):
        self.rotation_vector = LVecBase3f(0, 0, rot).normalized() * speed
