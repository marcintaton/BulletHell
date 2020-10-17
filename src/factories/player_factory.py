from src.ecs.entity import Entity
from src.ecs.components.transform import Transform
from src.ecs.components.sprite import Sprite


class PlayerFactory:

    def create_player(model, texture):
        player = Entity()
        player.add_component(Transform)
        player.add_component(Sprite, model, texture)
        return player
