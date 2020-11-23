from src.ecs.system import System
from src.ecs.components.transform import Transform
from src.ecs.components.player_data import PlayerData
from src.factories.bullet_factory import BulletFactory


class PlayerShootingSystem(System):

    required_components = [Transform, PlayerData]

    def __init__(self, ecs_manager):
        super().__init__(
            ecs_manager, __class__.required_components)
        self.bullets_fired = 0

    def execute(self):
        super().import_components()
        self.process_shooting_requests()

    def process_shooting_requests(self):
        for transform, player_data in zip(self.components[0], self.components[1]):
            if (player_data.fire_interval < player_data.current_fire_interval and player_data.requests_fire):
                forward = transform.forward()
                self.ecs_manager.add_entity(BulletFactory.create_player_bullet(
                    transform.position.x + transform.forward().x, transform.position.z + transform.forward().z, base.bullet_texture, forward.x, forward.z))
                player_data.current_fire_interval = 0
            else:
                player_data.current_fire_interval += globalClock.getDt()
            pass
