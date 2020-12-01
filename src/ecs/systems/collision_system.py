from src.ecs.system import System
from src.ecs.components.sphere_collider import SphereCollider
from src.ecs.components.box_collider import BoxCollider
from src.ecs.components.movement import Movement
from src.ecs.components.enemy_data import EnemyData
from src.utilities.tag_manager import TagManager
from src.ecs.components.player_data import PlayerData


class CollisionSystem(System):

    required_components = [SphereCollider]
    box_components = [BoxCollider]

    def __init__(self, ecs_manager):
        super().__init__(
            ecs_manager, __class__.required_components)
        self.box_colls_ids = self.parse_component_types(
            __class__.box_components)

    def execute(self):
        super().import_components()
        self.sphere_colliders = self.components[0]
        self.box_colliders = self.get_components_collection(
            self.box_colls_ids)[0]
        self.resolve_collisions()

    def resolve_collisions(self):
        player = [i for i in self.sphere_colliders if i.tag ==
                  TagManager.player][0]
        player_bullets = [i for i in self.sphere_colliders if i.tag ==
                          TagManager.player_bullet]
        enemies = [i for i in self.sphere_colliders if i.tag ==
                   TagManager.enemy]
        enemy_bullets_v = [i for i in self.sphere_colliders if i.tag ==
                           TagManager.enemy_bullet_violet]
        enemy_bullets_o = [i for i in self.sphere_colliders if i.tag ==
                           TagManager.enemy_bullet_orange]
        walls = self.box_colliders

        print(len(enemies))

        if len(enemies) is 0:
            player.parent.get_component(PlayerData).won = True

        for wall in walls:
            if (wall.is_colliding(player)):
                self.AABBPushOut(wall, player)

        for bullet in player_bullets:
            for wall in walls:
                if (wall.is_colliding(bullet)):
                    bullet.parent.active = False

            for enemy in enemies:
                if (enemy.is_colliding(bullet)):
                    enemy.parent.get_component(EnemyData).was_hit = True
                    bullet.parent.active = False

        for bullet in enemy_bullets_o:
            for wall in walls:
                if (wall.is_colliding(bullet)):
                    bullet.parent.active = False

            if bullet.is_colliding(player):
                player.parent.get_component(PlayerData).defeated = True

    def AABBPushOut(self, wall, player):
        player_trans = player.transform
        player_movement = player.parent.get_component(Movement)
        # TODO add wall sliding
        player_trans.position += player_movement.movement_vector * -1
