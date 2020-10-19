from src.ecs.entity import Entity
from src.ecs.components.transform import Transform
from src.ecs.components.sprite import Sprite
from src.ecs.components.movement import Movement
from src.ecs.components.player_data import PlayerData


class BulletFactory:

    def create_player_bullet(pos_x, pos_y, texture, mov_x, mov_y):
        bullet = Entity()
        bullet.add_component(Transform, pos_x, pos_y)
        bullet.add_component(Sprite, texture)
        bullet.add_component(Movement).set_movement(mov_x, mov_y, 0.15)
        return bullet
