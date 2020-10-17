from src.ecs.system import System
from src.ecs.components.transform import Transform
from src.ecs.components.movement import Movement
from src.ecs.components.player_data import PlayerData
from panda3d.core import LVector3f
from panda3d.core import LVector2f


class PlayerInputSystem(System):

    required_components = [Transform, Movement, PlayerData]

    def __init__(self, ecs_manager):
        super().__init__(
            ecs_manager, __class__.required_components)

    def set_player_input(self, player_input):
        self.player_input = player_input

    def execute(self):
        super().import_components()
        self.process_input()

    def process_input(self):

        left = self.player_input['left']
        right = self.player_input['right']
        up = self.player_input['up']
        down = self.player_input['down']
        fire = self.player_input['fire']
        mouse_x = self.player_input['mouse_x']
        mouse_y = self.player_input['mouse_y']

        for transform, movement, player_data in zip(self.components[0], self.components[1],  self.components[2]):
            movement.set_movement(
                (right - left), (up - down), player_data.speed * globalClock.getDt())

            player_vector = LVector2f(
                transform.position.x, transform.position.z)

            mouse_angle = LVector2f(mouse_x - transform.position.x / 10, mouse_y - transform.position.z / 10).signedAngleDeg(
                LVector2f(0, 1))
            transform.set_rotation(mouse_angle)

            player_data.requests_fire = bool(fire)
