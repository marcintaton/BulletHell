class EntityManager:

    def __init__(self):
        self.entities = []
        self.types = []
        self.component_containers = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update_refs(self):
        self.remove_inactive_ents()
        self.add_component_refs()
        self.remove_discarded_refs()

    def get_component_type_id(self, comp_type):
        try:
            return self.types.index(comp_type)
        except ValueError:
            self.types.append(comp_type)
            self.component_containers.append({})
            return len(self.types) - 1

    def remove_inactive_ents(self):
        for entity in self.entities:
            if not entity.active:
                entity.delete()
                self.entities.remove(entity)

    def add_component_refs(self):
        for entity in self.entities:
            for component in entity.components:
                type_id = self.get_component_type_id(type(component))
                if id(entity) not in self.component_containers[type_id].keys():
                    self.component_containers[type_id][id(entity)] = component

    def remove_discarded_refs(self):
        for comp_type in self.component_containers:
            for d_num, ref in list(comp_type.items()):
                if not ref.parent.active:
                    del comp_type[d_num]

    def get_components_for_types(self, type_ids):
        keys = self.get_ids_for_types(type_ids)
        components = [[] for _ in type_ids]
        for key in keys:
            for i, type_id in enumerate(type_ids):
                components[i].append(
                    self.component_containers[type_id][key])
        return components

    def get_ids_for_types(self, type_ids):
        intersection = []
        for type_id in type_ids:
            keys = set(self.component_containers[type_id].keys())
            if intersection == []:
                intersection = keys
            else:
                intersection &= keys
        return intersection
