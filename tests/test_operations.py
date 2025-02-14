from src.math_operations import add,sub

def test_add():
    assert add(1,2)==3
    assert add(-1,-2)==-3

def test_sub():
    assert sub(1,2)==-1
    assert sub(-1,-2)==1

