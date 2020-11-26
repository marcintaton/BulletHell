from src.ecs.entity import Entity
from src.ecs.components.transform import Transform
from src.ecs.components.sprite import Sprite
from src.ecs.components.box_collider import BoxCollider
from src.utilities.tag_manager import TagManager


class EnviroFactory:

    def create_wall(x, y, rotation, x_scale, y_scale, texture):
        wall = Entity()
        wall.add_component(Transform, x, y, rotation, x_scale, y_scale)
        wall.add_component(Sprite, texture)
        wall.add_component(BoxCollider, wall.get_component(
            Transform), TagManager.wall)
        return wall
