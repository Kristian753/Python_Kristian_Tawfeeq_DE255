from pytest import raises
from triangel import Triangle

def test_valid_init():
    triangle = Triangle(base = 5, height = 2)
    assert triangle.base == 5 and triangle.height == 2

def test_negative_base_fail():
    with raises(ValueError):
        Triangle(base=-1, height=2)

def test_negative_height_fail():
    with raises(ValueError):
        Triangle(base=1, height=-2)

def test_invalid_type_string_init_fail():
    with raises(TypeError):
        Triangle(base="1", height="two")

#def test_invalid_type_bool_init_fail():
 #   with raises(TypeError):
  #      Triangle(base=1, height=True)

def test_zero_base_fail():
    with raises(ValueError):
        Triangle(base=0, height=1)

def test_zero_height_fail():
    with raises(ValueError):
        Triangle(base=1, height=0)

def test_area_valid():
    triangle = Triangle(base = 2, height =3)
    assert triangle.area == 3

def test_equals_same_base_height():
    triangle1 = Triangle(base=2, height=3)
    triangle2 = Triangle(base=2, height=3)
    assert triangle1 == triangle2

def test_equals_same_base_height():
    assert Triangle(base=2,height=4)!=Triangle(base=1, height=8)

def test_lt_valid():
    triangel1 = Triangle(base=2, height=3)
    triangel2 = Triangle(base=3, height=4)
    assert triangel1 < triangel2

def test_le_same_value_valid():
    triangel1 = Triangle(base=2, height=3)
    triangel2 = Triangle(base=2, height=3)
    assert triangel1 <= triangel2

def test_le_different_value_valid():
    triangel1 = Triangle(base=1, height=3)
    triangel2 = Triangle(base=2, height=3)
    assert triangel1 <= triangel2

def test_gt_valid():
    triangel1 = Triangle(base=2, height=3)
    triangel2 = Triangle(base=3, height=4)
    assert triangel2 > triangel1

def test_ge_same_value_valid():
    triangel1 = Triangle(base=2, height=3)
    triangel2 = Triangle(base=2, height=3)
    assert triangel1 >= triangel2

def test_ge_different_value_valid():
    triangel1 = Triangle(base=4, height=3)
    triangel2 = Triangle(base=2, height=3)
    assert triangel1 >= triangel2