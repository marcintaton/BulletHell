from src.ecs.system import System
from src.ecs.components.transform import Transform
from src.ecs.components.movement import Movement


class MovementSystem(System):

    required_components = [Transform, Movement]

    def __init__(self, ecs_manager):
        super().__init__(
            ecs_manager, __class__.required_components)

    def execute(self):
        super().import_components()
        self.apply_movement()

    def apply_movement(self):
        for transform, movement in zip(self.components[0], self.components[1]):
            print(transform.rotation, movement.rotation_vector)
            transform.position += movement.movement_vector
            transform.rotation += movement.rotation_vector
