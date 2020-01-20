# Implement the first move model for the Lego robot.
# 02_a_filter_motor
# Claus Brenner, 31 OCT 2012
from math import sin, cos, pi
from pylab import *
from lego_robot import *

# This function takes the old (x, y, heading) pose and the motor ticks
# (ticks_left, ticks_right) and returns the new (x, y, heading).
def filter_step(old_pose, motor_ticks, ticks_to_mm, robot_width):

    # Find out if there is a turn at all.
    if motor_ticks[0] == motor_ticks[1]:
        # No turn. Just drive straight.

        # --->>> Implement your code to compute x, y, theta here.
        theta = old_pose[2]
        x = old_pose[0] + motor_ticks[0] * ticks_to_mm * cos(theta)
        y = old_pose[1] + motor_ticks[0] * ticks_to_mm * sin(theta)
        return (x, y, theta)

    else:
        # Turn. Compute alpha, R, etc.

        # --->>> Implement your code to compute x, y, theta here.
        
        theta = old_pose[2]
        x = old_pose[0]
        y = old_pose[1]
        l = motor_ticks[0] * ticks_to_mm
        r = motor_ticks[1] * ticks_to_mm
        alpha = (r - l) / robot_width
        R = l / alpha
        C = [x - (R+robot_width/2)*sin(theta), y - (R+robot_width/2)*(-cos(theta))]
        theta = (theta + alpha) % (2*pi)
        x = C[0] + (R+robot_width/2)*sin(theta)
        y = C[1] + (R+robot_width/2)*(-cos(theta))
        return (x, y, theta)

if __name__ == '__main__':
    # Empirically derived conversion from ticks to mm.
    ticks_to_mm = 0.349

    # Measured width of the robot (wheel gauge), in mm.
    robot_width = 150.0

    # Read data.
    logfile = LegoLogfile()
    logfile.read("robot4_motors.txt")

    # Start at origin (0,0), looking along x axis (alpha = 0).
    pose = (0.0, 0.0, 0.0)

    # Loop over all motor tick records generate filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks, ticks_to_mm, robot_width)
        filtered.append(pose)

    # Draw result.
    for pose in filtered:
        print(pose)
        plot([p[0] for p in filtered], [p[1] for p in filtered], 'bo')
    show()
