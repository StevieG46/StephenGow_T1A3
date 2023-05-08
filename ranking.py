class Ranking:
    def __init__(self):
        self.events = []
        self.athletes = []

    def add_event(self, event_name, points_for_1st, points_for_2nd, points_for_3rd):
        event = Event(event_name, points_for_1st, points_for_2nd, points_for_3rd)
        self.events.append(event)

    def update_event_scores(self, event_name, athlete_scores):
        event = next((e for e in self.events if e.name == event_name), None)
        if event is not None:
            for athlete_name, scores in athlete_scores.items():
                athlete = next((a for a in self.athletes if a.name == athlete_name), None)
                if athlete is None:
                    athlete = Athlete(athlete_name)
                    self.athletes.append(athlete)
                athlete.scores.append((event_name, scores))
                event.athletes.append(athlete)
                self.calculate_total_points(athlete)
            self.rank_athletes()