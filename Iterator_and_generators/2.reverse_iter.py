class reverse_iter:
    def __init__(self, iter):
        self.iter = iter
        self.i = len(self.iter) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 0:
            raise StopIteration
        value = self.iter[self.i]
        self.i -= 1
        return value


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
