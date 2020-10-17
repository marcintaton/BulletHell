from panda3d.core import loadPrcFileData
from BulletHellGame import BulletHellGame
from src.ecs.entity_manager import EntityManager
from src.ecs.system_manager import SystemManager
from pandac.PandaModules import *

entity_manager = EntityManager()
system_manager = SystemManager()

ConfigVariableString("window-title", "Panda").setValue("Client")
ConfigVariableString(
    "win-size", "500 400").setValue(str(900) + " " + str(900))
loadPrcFileData('', 'win-fixed-size 1')
game = BulletHellGame(entity_manager, system_manager)
game.run()
