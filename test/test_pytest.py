from src.calculator import fun1, fun2, fun3, fun4, fun5, fun6, fun7, fun8


def test_fun1():
    assert fun1(2, 3) == 5


def test_fun2():
    assert fun2(5, 3) == 2


def test_fun3():
    assert fun3(4, 3) == 12


def test_fun4():
    assert fun4(1, 2, 3) == 6


def test_fun5():
    assert fun5(10, 2) == 5


def test_fun6():
    assert fun6(2, 3) == 8


def test_fun7():
    assert fun7(10, 3) == 1


def test_fun8():
    assert fun8(10, 20) == 15