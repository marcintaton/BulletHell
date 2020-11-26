from src.ecs.component import Component
import src.ecs.components.sphere_collider as SphereCollider
from panda3d.core import Point2


class BoxCollider(Component):

    def __init__(self, parent, transform, tag="default"):
        super().__init__(parent)
        self.tag = tag
        self.transform = transform

    @property
    def top(self):
        return self.transform.position.z + self.transform.scale.z / 2

    @property
    def bottom(self):
        return self.transform.position.z - self.transform.scale.z / 2

    @property
    def left(self):
        return self.transform.position.x - self.transform.scale.x / 2

    @property
    def right(self):
        return self.transform.position.x + self.transform.scale.x / 2

    def is_colliding(self, other):
        if (isinstance(other, BoxCollider)):
            # print("Box colliding vs Box")
            pass

        if(isinstance(other, SphereCollider.SphereCollider)):

            result = False

            if self.right > other.left and self.left < other.left and self.top > other.bottom and self.bottom < other.top:
                # print("Right collision")
                result = True

            if self.left < other.right and self.right > other.right and self.top > other.bottom and self.bottom < other.top:
                # print("Left collision")
                result = True

            if self.top > other.bottom and self.bottom < other.bottom and self.left < other.right and self.right > other.left:
                # print("Top collision")
                result = True

            if self.bottom < other.top and self.top > other.top and self.left < other.right and self.right > other.left:
                # print("Bottom collision")
                result = True

            return result
