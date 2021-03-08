class Trainer:
    next_id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        Trainer.next_id += 1
        return Trainer.next_id
