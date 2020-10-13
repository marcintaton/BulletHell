class SystemManager:

    def __init__(self):
        self.systems = []

    def add_system(self, system):
        self.systems.append(system)

    def execute_all(self):
        for system in self.systems:
            system.execute()
