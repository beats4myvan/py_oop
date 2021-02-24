class Cup:
    def __init__(self, size, quntity):
        self.size = size
        self.quntity = quntity

    def fill(self, milliliters):
        if self.quntity + milliliters <= self.size:
            self.quntity += milliliters


    def status(self):
        free_space = self.size - self.quntity
        return free_space


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
