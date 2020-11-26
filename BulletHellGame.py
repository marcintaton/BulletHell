from direct.task.Task import TaskManager
from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode, TransparencyAttrib
from direct.task.TaskManagerGlobal import taskMgr
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import WindowProperties
from panda3d.core import GraphicsWindow
import sys

# temp imports refactor and remove later
from src.factories.player_factory import PlayerFactory
from src.factories.enviro_factory import EnviroFactory
from src.factories.enemy_factory import EnemyFactory

from src.ecs.components.sprite import Sprite
from src.ecs.components.transform import Transform

from src.ecs.systems.positioning_system import PositioningSystem
from src.ecs.systems.player_input_system import PlayerInputSystem
from src.ecs.systems.movement_system import MovementSystem
from src.ecs.systems.player_shooting_system import PlayerShootingSystem
from src.ecs.systems.collision_system import CollisionSystem
from src.ecs.systems.enemy_management_system import EnemyManagementSystem
from panda3d.core import LVecBase3f


class BulletHellGame(ShowBase):

    def __init__(self, entity_manager, system_manager):
        ShowBase.__init__(self)
        self.base = self
        self.task_manager = TaskManager()
        self.entity_manager = entity_manager
        self.system_manager = system_manager
        self.game_loop_running = False
        self.temporatySetup()

    def run(self):
        self.game_loop_running = True
        self.gameLoop()

    def handleEvents(self):
        self.handleMouse()

    def handleMouse(self):
        if self.base.mouseWatcherNode.hasMouse():
            self.setInputValue(
                "mouse_x", self.base.mouseWatcherNode.getMouseX())
            self.setInputValue(
                "mouse_y", self.base.mouseWatcherNode.getMouseY())

    def gameLoop(self):

        timer = 0

        while self.game_loop_running:

            timer += globalClock.getDt()
            self.sample_text.setText(str(timer))

            self.handleEvents()

            self.entity_manager.update_refs()
            self.system_manager.execute_all()

            self.task_manager.step()

    # temp setup method, for pretty much everything
    # refactor and remove later
    def temporatySetup(self):
        # mouse stuff
        self.base.disableMouse()

        wp = WindowProperties()
        # wp.setCursorHidden(True)
        wp.setMouseMode(WindowProperties.M_confined)
        self.base.win.requestProperties(wp)

        # gui :)
        self.sample_text = OnscreenText(text="0", parent=self.base.a2dTopLeft, pos=(0.07, -.06 * 0 - 0.1),
                                        fg=(1, 1, 1, 1), align=TextNode.ALeft, shadow=(0, 0, 0, 0.5), scale=.05, mayChange=1)

        self.plane_model = loader.loadModel("models/plane")
        self.player_texture = loader.loadTexture("textures/ship.png")
        self.bullet_texture = loader.loadTexture("textures/bullet.png")
        self.wall_texture = loader.loadTexture("textures/wall.png")
        self.enemy_texture = loader.loadTexture("textures/enemy_turret.png")
        self.orange_bullet_texture = loader.loadTexture(
            "textures/orange_bullet.png")

        # input handling setup
        self.player_input = {"left": 0, "right": 0,
                             "up": 0, "down": 0, "fire": 0, "mouse_x": 0, "mouse_y": 0}
        self.accept("escape", sys.exit)  # Escape quits
        # Other keys events set the appropriate value in our key dictionary
        self.accept("arrow_left",     self.setInputValue, ["left", 1])
        self.accept("arrow_left-up",  self.setInputValue, ["left", 0])
        self.accept("arrow_right",    self.setInputValue, ["right", 1])
        self.accept("arrow_right-up", self.setInputValue, ["right", 0])
        self.accept("arrow_up",       self.setInputValue, ["up", 1])
        self.accept("arrow_up-up",    self.setInputValue, ["up", 0])
        self.accept("arrow_down",       self.setInputValue, ["down", 1])
        self.accept("arrow_down-up",    self.setInputValue, ["down", 0])
        self.accept("mouse3",          self.setInputValue, ["fire", 1])
        self.accept("mouse3-up",          self.setInputValue, ["fire", 0])

        # systems
        plInput = PlayerInputSystem(self.entity_manager)
        plInput.set_player_input(self.player_input)
        plInput.set_base(self.base)

        self.system_manager.add_system(plInput)
        self.system_manager.add_system(MovementSystem(self.entity_manager))
        self.system_manager.add_system(PositioningSystem(self.entity_manager))
        self.system_manager.add_system(
            PlayerShootingSystem(self.entity_manager))
        self.system_manager.add_system(CollisionSystem(self.entity_manager))
        self.system_manager.add_system(
            EnemyManagementSystem(self.entity_manager))

        # entities
        # player
        self.player = PlayerFactory.create_player(self.player_texture)
        self.entity_manager.add_entity(self.player)

        wall0 = EnviroFactory.create_wall(10, 0, 0, 1, 21, self.wall_texture)
        wall1 = EnviroFactory.create_wall(-10, 0, 0, 1, 21, self.wall_texture)
        wall2 = EnviroFactory.create_wall(0, 10, 0, 21, 1, self.wall_texture)
        wall3 = EnviroFactory.create_wall(0, -10, 0, 21, 1, self.wall_texture)
        self.entity_manager.add_entity(wall0)
        self.entity_manager.add_entity(wall1)
        self.entity_manager.add_entity(wall2)
        self.entity_manager.add_entity(wall3)

        enemy1 = EnemyFactory.create_turret(5, 5, self.enemy_texture)
        self.entity_manager.add_entity(enemy1)

    def setInputValue(self, input, val):
        self.player_input[input] = val
