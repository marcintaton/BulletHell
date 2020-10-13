from BulletHellGame import BulletHellGame
from src.ecs.entity_manager import EntityManager
from src.ecs.system_manager import SystemManager

entity_manager = EntityManager()
system_manager = SystemManager()

game = BulletHellGame(entity_manager, system_manager)
game.run()
