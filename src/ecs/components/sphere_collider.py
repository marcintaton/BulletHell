from src.ecs.component import Component
import src.ecs.components.box_collider as BoxCollider


class SphereCollider(Component):

    def __init__(self, parent, transform, tag="default"):
        super().__init__(parent)
        self.tag = tag
        self.transform = transform

    @property
    def top(self):
        return self.transform.position.z + self.radius

    @property
    def bottom(self):
        return self.transform.position.z - self.radius

    @property
    def left(self):
        return self.transform.position.x - self.radius

    @property
    def right(self):
        return self.transform.position.x + self.radius

    @property
    def center(self):
        return self.transform.position.xz

    @property
    def radius(self):
        return self.transform.scale.x / 2

    def is_colliding(self, other):
        if (isinstance(other, BoxCollider.BoxCollider)):
            # print("Sphere colliding vs Box")
            pass

        if(isinstance(other, SphereCollider)):
            other_radius = other.radius
            this_radius = self.radius

            other_center = other.center
            this_center = self.center

            return (other_center - this_center).length() <= (this_radius + other_radius)
