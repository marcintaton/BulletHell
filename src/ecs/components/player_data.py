from src.ecs.component import Component


class PlayerData(Component):

    def __init__(self, parent):
        super().__init__(parent)
        self.max_hp = 3
        self.current_hp = self.max_hp
        self.speed = 10
        self.requests_fire = False
        self.fire_interval = 0.1
        self.current_fire_interval = 0
