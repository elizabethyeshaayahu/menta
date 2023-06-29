from datetime import datetime


class TruePoint:
    def __init__(self, point_id: int, time: datetime, time_second: int, x: float, y: float, space_x: float,
                 space_y: float):
        self.point_id = point_id
        self.time = time
        self.time_second = time_second
        self.x = x
        self.y = y
        self.space_x = space_x
        self.space_y = space_y

