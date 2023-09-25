def test_add():
    assert (add(1, 2)) == 3


def test_divide():
    assert (div(2.3, 1)) == 2.3


def add(x, y):
    return x + y


def div(x, y):
    if y == 0:
        print("Nie dzielimy przez zero")
    else:
        return x / y
