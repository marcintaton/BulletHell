class System:

    def __init__(self, ecs_manager, required_components):
        self.ecs_manager = ecs_manager
        self.comp_ids = self.parse_component_types(required_components)

    def execute(self):
        pass

    def parse_component_types(self, types):
        ids = []
        for comp_type in types:
            ids.append(self.ecs_manager.get_component_type_id(comp_type))
        return ids

    def import_components(self):
        self.components = self.ecs_manager.get_components_for_types(
            self.comp_ids)

    def get_components_collection(self, ids):
        return self.ecs_manager.get_components_for_types(ids)
