class Event:
    def __init__(self, name, points_for_1st, points_for_2nd, points_for_3rd):
        self.name = name
        self.points = [points_for_1st, points_for_2nd, points_for_3rd]
        self.athletes = []