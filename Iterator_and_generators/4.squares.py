def squares(num):
    # squares_num = [i * i for i in range(1, num+1)]
    # for num in squares_num:
    #     yield num
    i = 1
    while i <= num:
        yield i * i
        i += 1


print(list(squares(5)))
