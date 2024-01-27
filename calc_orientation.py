import numpy as np
from numpy.typing import NDArray
import math
# assuming diagonal placement of the receiver.
# 
# head ------- 
# |           |
# |           |
#   --------- tail
# return the angle of the robot in radian
# maybe not use NDArray
def calc_orientation(head_pos: NDArray, tail_pos: NDArray, robot_width, robot_length):
    # diagonal angle offset: the diff. in angle between angle of diagonal of robot
    # calculated from the actual orientation of the robot
    dia_angle_offset = np.arctan(robot_width, robot_length)
    
    # vector from tail to head
    t_h_vec = head_pos - tail_pos
    # note that for arctan2 the position of y and x are swapped
    # return the angle from x axis in radian
    diagonal_orientation = np.arctan2(t_h_vec[1], t_h_vec[0])

    return diagonal_orientation - dia_angle_offset
