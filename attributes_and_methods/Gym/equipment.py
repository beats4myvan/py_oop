class Equipment:
    equipment_id_counter = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.equipment_id_counter += 1
        return Equipment.equipment_id_counter

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
