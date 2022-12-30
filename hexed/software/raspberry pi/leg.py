#!python
#
# 2021  Zhengyu Peng
# Website: https://zpeng.me
#
# `                      `
# -:.                  -#:
# -//:.              -###:
# -////:.          -#####:
# -/:.://:.      -###++##:
# ..   `://:-  -###+. :##:
#        `:/+####+.   :##:
# .::::::::/+###.     :##:
# .////-----+##:    `:###:
#  `-//:.   :##:  `:###/.
#    `-//:. :##:`:###/.
#      `-//:+######/.
#        `-/+####/.
#          `+##+.
#           :##:
#           :##:
#           :##:
#           :##:
#           :##:
#            .+:

import numpy as np
 

class Leg:
    def __init__(self,
                 id,
                 junction_servos,
                 correction=[0, 0, 0],
                 scale=[1, 1, 1],
                 constraint=[[35, 145], [0, 165], [30, 150]]):
        self.id = id
        self.junction_servos = junction_servos
        self.correction = correction
        self.constraint = constraint

    def set_angle(self, junction, angle):
        set_angle = np.min(
            [angle+self.correction[junction], self.constraint[junction][1]+self.correction[junction], 180])
        set_angle = np.max(
            [set_angle, self.constraint[junction][0]+self.correction[junction], 0])
        self.junction_servos[junction].angle = set_angle

    def set_raw_angle(self, junction, angle):
        self.junction_servos[junction].angle = angle

    def move_junctions(self, angles):
        self.set_angle(0, angles[0])
        self.set_angle(1, angles[1])
        self.set_angle(2, angles[2])

    def reset(self, calibrated=False):
        if calibrated:
            self.set_angle(0, 90)
            self.set_angle(1, 90)
            self.set_angle(2, 90)
        else:
            self.set_raw_angle(0, 90)
            self.set_raw_angle(1, 90)
            self.set_raw_angle(2, 90)
