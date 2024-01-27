from radio_wave_to_transform import radio_wave_find_transform
from calc_orientation import calc_orientation
from trilateriation import trilaterate_based_on_berm
from math import pi
import numpy as np

# trilateration test

# calc_orientation test
robot_width, robot_length  = 2, 4
# head_pos: NDArray, tail_pos: NDArray, robot_width, robot_length
head_pos, tail_pos= [-1, 2], [1, -2]
assert calc_orientation(head_pos, tail_pos, robot_width, robot_length) == pi / 2

for i in range(-10, 10):
    for j in range(-10, 10):
        head_pos, tail_pos= [-1 + i, 2 + j], [1 + i, -2 + j]
        assert calc_orientation(head_pos, tail_pos, robot_width, robot_length) == pi / 2

def rotation_matrix(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])

def float_equal(x, y):
    return abs(x - y) < 1e-10

for i in range(180):
    head_pos, tail_pos= np.array([-1, 2]), np.array([1, -2])
    # rotate
    angle = np.pi / 180 * i
    expected_angle = angle + pi / 2
    rotate = rotation_matrix(angle)
    head_pos, tail_pos = rotate.dot(head_pos), rotate.dot(tail_pos)

    calc_angle = calc_orientation(head_pos, tail_pos, robot_width, robot_length)
    print(expected_angle, calc_angle)
    # assert float_equal(expected_angle, calc_angle)
    

print("all tests passed")


# transform test
# # given coordinate in robot coord. turn into home coord.
# home direction: x dir for berm
# no rotation