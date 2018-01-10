def fib(number):
    first = 0
    next1 = 1
    if number == 0:
        return first
    elif number == 1:
        return next1
    else:
        for i in range(2, number):
            first, next1 = next1, first+next1
    return next1


print(fib(7))



