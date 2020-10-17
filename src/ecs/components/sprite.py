from panda3d.core import TransparencyAttrib
from src.ecs.component import Component


class Sprite(Component):

    def __init__(self, parent, model, texture):
        super().__init__(parent)
        self.texture = texture
        self.render_object = model
        self.render_object.reparentTo(camera)
        self.render_object.setBin("unsorted", 0)
        self.render_object.setDepthTest(False)
        self.render_object.setTransparency(TransparencyAttrib.MAlpha)
        self.render_object.setTexture(self.texture, 1)