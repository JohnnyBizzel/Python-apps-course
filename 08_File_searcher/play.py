# Calculate Fibonacci series


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        # use tuple projection
        current, next = next, next + current
        nums.append(current)

    return nums


print('with lists')
for n in fibonacci(100):
    print(n, end=', ')


# Co method!

def fibonacci_co():

    current = 0
    next_ = 1

    while True:
        # use tuple projection
        current, next_ = next_, next_ + current
        # doesn't hold all results in memory
        yield current


print()
print('with yield')
for n in fibonacci_co():
    if n > 2550000:
        break

    print(n, end=', ')
