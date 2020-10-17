from src.ecs.system import System
from src.ecs.components.transform import Transform
from src.ecs.components.sprite import Sprite


class PositioningSystem(System):

    required_components = [Transform, Sprite]

    def __init__(self, ecs_manager):
        super().__init__(
            ecs_manager, __class__.required_components)

    def execute(self):
        super().import_components()
        self.position_elements()

    def position_elements(self):
        for transform, sprite in zip(self.components[0], self.components[1]):
            sprite.render_object.setPos(transform.position)
            sprite.render_object.setScale(transform.scale)
            sprite.render_object.setHpr(transform.rotation)
