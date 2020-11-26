from src.ecs.component import Component


class EnemyData(Component):

    def __init__(self, parent, hp, shooting_directions=[]):
        super().__init__(parent)
        self.hit_points = hp
        self.was_hit = False
        self.shooting_directions = shooting_directions
        self.fire_interval = 0.3
        self.current_fire_interval = 0
