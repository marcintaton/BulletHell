from panda3d.core import LVector3f
from src.ecs.component import Component
import math

DEPTH = 50


class Transform(Component):
    def __init__(self, parent, x=0, y=0, rotation=0, scale_x=1, scale_y=1):
        super().__init__(parent)
        self.position = LVector3f(x, DEPTH, y)
        self.rotation = rotation
        self.scale = LVector3f(scale_x, 1, scale_y)

    def set_position(self, x, y):
        self.position = LVector3f(x, DEPTH, y)

    def set_scale(self, x, y):
        self.scale = LVector3f(x, 1, y)

    def set_rotation(self, rot):
        if rot < 0:
            rot = 360 + rot
        self.rotation = rot

    def forward(self):
        angle = math.radians(self.rotation)
        forward_x = math.sin(angle)
        forward_z = math.cos(angle)
        # print(self.rotation, angle, LVector3f(forward_x, 0, forward_z))
        # print(self.position)
        return LVector3f(forward_x, 0, forward_z)
