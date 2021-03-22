class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_count = 0
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count == self.count:
            raise StopIteration
        temp = self.current_value
        self.current_value += self.step
        self.current_count += 1
        return temp


#
numbers = take_skip(2, 6)
for number in numbers:
    print(number)
# test zero
# import unittest
#
# class TakeSkipTests(unittest.TestCase):
#     def test_zero(self):
#         numbers = take_skip(2, 6)
#         res = []
#         for number in numbers:
#             res.append(number)
#         self.assertEqual(res, [0, 2, 4, 6, 8, 10])
#
# if __name__ == '__main__':
#     unittest.main()
