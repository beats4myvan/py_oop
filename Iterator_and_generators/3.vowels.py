class vowels:
    vowels = {'a', 'A', 'Y', 'y', 'u', 'U', 'e', 'E', 'i', 'I', 'o', 'O'}

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        ch = self.text[self.index]
        self.index += 1
        if ch not in self.vowels:
            return self.__next__()
        return ch

# def vowels(text):
#     vovels = {'a', 'A', 'Y', 'y', 'u', 'U', 'e', 'E', 'i', 'I', 'o', 'O'}
#     for ch in text:
#         if ch in vovels:
#             yield ch


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
