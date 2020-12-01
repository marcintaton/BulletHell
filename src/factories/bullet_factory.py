from src.ecs.entity import Entity
from src.ecs.components.transform import Transform
from src.ecs.components.sprite import Sprite
from src.ecs.components.movement import Movement
from src.ecs.components.sphere_collider import SphereCollider
from src.utilities.tag_manager import TagManager


class BulletFactory:

    def create_player_bullet(pos_x, pos_y, texture, mov_x, mov_y):
        bullet = Entity()
        bullet.add_component(Transform, pos_x, pos_y, 0, 0.25, 0.25)
        bullet.add_component(Sprite, texture)
        bullet.add_component(Movement).set_movement(mov_x, mov_y, 0.25)
        bullet.add_component(SphereCollider, bullet.get_component(
            Transform), TagManager.player_bullet)
        return bullet

    def create_orange_bullet(pos_x, pos_y, texture, mov_x, mov_y):
        bullet = Entity()
        bullet.add_component(Transform, pos_x, pos_y, 0, 0.5, 0.5)
        bullet.add_component(Sprite, texture)
        bullet.add_component(Movement).set_movement(mov_x, mov_y, 0.15)
        bullet.add_component(SphereCollider, bullet.get_component(
            Transform), TagManager.enemy_bullet_orange)
        return bullet
