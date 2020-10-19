from src.ecs.entity import Entity
from src.ecs.components.transform import Transform
from src.ecs.components.sprite import Sprite
from src.ecs.components.movement import Movement
from src.ecs.components.player_data import PlayerData


class PlayerFactory:

    def create_player(texture):
        player = Entity()
        player.add_component(Transform)
        player.add_component(Sprite, texture)
        player.add_component(Movement)
        player.add_component(PlayerData)
        return player
