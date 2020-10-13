from direct.task.Task import TaskManager
from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode, TransparencyAttrib
from direct.gui.OnscreenText import OnscreenText
import sys


class BulletHellGame(ShowBase):

    def __init__(self, entity_manager, system_manager):
        ShowBase.__init__(self)
        self.task_manager = TaskManager()
        self.entity_manager = entity_manager
        self.system_manager = system_manager
        self.game_loop_running = False

        self.sample_text = OnscreenText(text="0", parent=base.a2dTopLeft, pos=(0.07, -.06 * 0 - 0.1),
                                        fg=(1, 1, 1, 1), align=TextNode.ALeft, shadow=(0, 0, 0, 0.5), scale=.05, mayChange=1)

    def run(self):
        self.game_loop_running = True
        self.gameLoop()

    def gameLoop(self):

        timer = 0

        while self.game_loop_running:

            timer += globalClock.getDt()
            self.sample_text.setText(str(timer))

            self.entity_manager.update_refs()
            self.system_manager.execute_all()

            self.task_manager.step()
