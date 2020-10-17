from panda3d.core import LVecBase3f
from src.ecs.component import Component

DEPTH = 50


class Transform(Component):
    def __init__(self, parent, x=0, y=0, rotation=0, scale_x=1, scale_y=1):
        super().__init__(parent)
        self.position = LVecBase3f(x, DEPTH, y)
        self.rotation = LVecBase3f(0, 0, rotation)
        self.scale = LVecBase3f(scale_x, 1, scale_y)

    def set_position(self, x, y):
        self.position = LVecBase3f(x, DEPTH, y)

    def set_scale(self, x, y):
        self.scale = LVecBase3f(x, 1, y)

    def set_rotation(self, rot):
        self.rotation = LVecBase3f(0, 0, rot)
