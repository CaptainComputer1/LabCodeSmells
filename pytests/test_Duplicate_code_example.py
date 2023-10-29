import time
from Old_Code.Duplicate_code_example import *
from New_Code.Efficient_Shape_Code import *
def test_calculate_area():
    assert calculate_area(3, 5) == 15
def test_calculate_perimeter():
    assert calculate_perimeter(3,5) == 16
def test_calculate_volume():
    assert calculate_volume(3,5,7) == 105
def test_calculate_surface_area():
    assert calculate_surface_area(3,5,7) == 142

def test_calculate_shape_measurement():
    assert calculate_shape_measurement("area", 3,5) == 15
    assert calculate_shape_measurement("perimeter", 3,5) == 16
    assert calculate_shape_measurement("volume", 3,5,7) == 105
    assert calculate_shape_measurement("surface area", 3,5,7) == 142
    assert calculate_shape_measurement("dimension", 3,5,7) == "Please specify a valid shape measurement, such as area, perimeter, volume or surface area."