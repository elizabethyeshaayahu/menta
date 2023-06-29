from datetime import datetime

import numpy as np

from true_points import TruePoint


class EstimatePoint:
    def __init__(self, point_id: int, time: datetime, time_second: int, minor: int, major: int,
                 azimuth: float, x: float, y: float, space_x: float, space_y: float):
        self.point_id = point_id
        self.time = time
        self.time_second = time_second
        self.minor = minor
        self.major = major
        self.azimuth = azimuth
        self.x = x
        self.y = y
        self.space_x = space_x
        self.space_y = space_y

    def isTimeDiffValid(self, true_point: TruePoint):
        if (np.absolute((true_point.time - self.time).total_seconds()) > 1800):
            return False
        else:
            return True
