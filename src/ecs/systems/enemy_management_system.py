from src.ecs.system import System
from src.ecs.components.enemy_data import EnemyData
from src.ecs.components.transform import Transform
from src.factories.bullet_factory import BulletFactory


class EnemyManagementSystem(System):

    required_components = [EnemyData, Transform]

    def __init__(self, ecs_manager):
        super().__init__(
            ecs_manager, __class__.required_components)

    def execute(self):
        super().import_components()
        self.resolve_hits()
        self.resolve_shots()

    def resolve_hits(self):
        for enemy_data in self.components[0]:

            if enemy_data.was_hit is True:
                enemy_data.was_hit = False
                enemy_data.hit_points -= 1
                if enemy_data.hit_points == 0:
                    enemy_data.parent.active = False

    def resolve_shots(self):
        for enemy_data, transform in zip(self.components[0], self.components[1]):
            if enemy_data.fire_interval < enemy_data.current_fire_interval:
                self.ecs_manager.add_entity(BulletFactory.create_orange_bullet(
                    transform.position.x + transform.right.x, transform.position.z + transform.right.z, base.orange_bullet_texture, transform.right.x, transform.right.z))

                self.ecs_manager.add_entity(BulletFactory.create_orange_bullet(
                    transform.position.x + transform.left.x, transform.position.z + transform.left.z, base.orange_bullet_texture, transform.left.x, transform.left.z))

                self.ecs_manager.add_entity(BulletFactory.create_orange_bullet(
                    transform.position.x + transform.forward.x, transform.position.z + transform.forward.z, base.orange_bullet_texture, transform.forward.x, transform.forward.z))

                self.ecs_manager.add_entity(BulletFactory.create_orange_bullet(
                    transform.position.x + transform.backward.x, transform.position.z + transform.backward.z, base.orange_bullet_texture, transform.backward.x, transform.backward.z))

                enemy_data.current_fire_interval = 0
            else:
                enemy_data.current_fire_interval += globalClock.getDt()
