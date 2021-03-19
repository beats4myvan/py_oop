def genrange(start, end):
    list_nums = [i for i in range(start, end + 1)]
    for num in list_nums:
        yield num




print(list(genrange(1, 10)))

# def first_n(n):
#     num = 0
#
#     while num < n:
#         yield num
#
#         num += 1
#
#
# sum_first_n = sum(first_n(5))
#
# print(sum_first_n)
