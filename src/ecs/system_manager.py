class SystemManager:

    def __init__(self):
        self.systems = []
        self.active = True

    def add_system(self, system):
        self.systems.append(system)

    def execute_all(self):
        if self.active is False:
            return

        for system in self.systems:
            system.execute()
