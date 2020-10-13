class Entity:

    def __init__(self):
        self.active = True
        self.components = []

    def has_component(self, type):
        return any(isinstance(x, type) for x in self.components)

    def add_component(self, type, *args):
        self.components.append(type(self, *args))

    def get_component(self, type):
        return next(x for x in self.components if isinstance(x, type))

    def remove_component(self, type):
        self.components = [
            x for x in self.components if not isinstance(x, type)]
