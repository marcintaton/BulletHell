from src.ecs.system import System
from src.ecs.components.player_data import PlayerData
import BulletHellGame


class LevelCompleteSystem(System):

    required_components = [PlayerData]

    def __init__(self, ecs_manager):
        super().__init__(
            ecs_manager, __class__.required_components)

    def execute(self):
        super().import_components()
        self.check_status()

    def check_status(self):

        player_data = self.components[0][0]

        if player_data.defeated == True:
            BulletHellGame.BulletHellGame.Instance.onPlayerDeath()
        elif player_data.won == True:
            BulletHellGame.BulletHellGame.Instance.onLevelComplete()
