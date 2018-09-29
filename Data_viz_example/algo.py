realNumberArray = [4, 5.6, -9.8, 3.14, 42, 6, 8.34]


def square_list(arr):
    ints = (
        num
        for num in realNumberArray
        if isinstance(num, int)  # test (if integer)
    )

    for el in ints:
        if el > 0:
            yield el**2


print(list(square_list(realNumberArray)))  # [16, 1764, 36]
