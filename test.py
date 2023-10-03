import math

def test_sqrt():
    num=25
    assert math.sqrt(num) == 6

def test_square():
    num = 7
    assert num*num == 50

def test_check():
    x = 90

    assert x>=100

def test_multiply():
    a=4
    b=5

    assert a*b == 25

def test_fun():
    c=9

    assert c+1 == 11