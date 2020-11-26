from src.ecs.entity import Entity
from src.ecs.components.transform import Transform
from src.ecs.components.sprite import Sprite
from src.ecs.components.sphere_collider import SphereCollider
from src.ecs.components.enemy_data import EnemyData
from src.ecs.components.movement import Movement
from src.utilities.tag_manager import TagManager


class EnemyFactory:

    def create_turret(pos_x, pos_y, texture, rotation=0.1):
        enemy = Entity()
        enemy.add_component(Transform, pos_x, pos_y, 0, 1, 1)
        enemy.add_component(Sprite, texture)
        enemy.add_component(EnemyData, 10, ["left"])
        enemy.add_component(Movement).set_rotation(rotation)
        enemy.add_component(SphereCollider, enemy.get_component(
            Transform), TagManager.enemy)
        return enemy
