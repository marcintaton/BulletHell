class Entity:

    def __init__(self):
        self.active = True
        self.components = []

    def has_component(self, type):
        return any(isinstance(x, type) for x in self.components)

    def add_component(self, type, *args):
        component = type(self, *args)
        self.components.append(component)
        return component

    def get_component(self, type):
        return next(x for x in self.components if isinstance(x, type))

    def remove_component(self, type):
        self.components = [
            x for x in self.components if not isinstance(x, type)]

    def delete(self):
        for c in self.components:
            c.on_delete()
