class Athlete:
    def __init__(self, name):
        self.name = name
        self.scores = []
        self.total_points = 0
        self.rank = None

class Event:
    def __init__(self, name, points_for_1st, points_for_2nd, points_for_3rd):
        self.name = name
        self.points = [points_for_1st, points_for_2nd, points_for_3rd]
        self.athletes = []

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

    def add_athlete(self, athlete_name):
        athlete = next((a for a in self.athletes if a.name == athlete_name), None)
        if athlete is None:
            athlete = Athlete(athlete_name)
            self.athletes.append(athlete)
   
    def update_athlete_scores(self, athlete_name, event_name, score):
        athlete = next((a for a in self.athletes if a.name == athlete_name), None)
        if athlete is None:
            athlete = Athlete(athlete_name)
            self.athletes.append(athlete)
        event = next((e for e in self.events if e.name == event_name), None)
        if event is None:
            print(f"Event '{event_name}' not found.")
            return
        athlete.scores.append((event_name, score))
        if athlete not in event.athletes:
            event.athletes.append(athlete)
        self.calculate_total_points(athlete)
        self.rank_athletes()

    # def update_athlete_scores(self, athlete_name, event_name):
    #     with open('data.txt', 'r') as f:
    #         lines = f.readlines()
    #     for line in lines:
    #         data = line.strip().split(',')
    #         if data[0] == event_name:
    #             points_for_1st = int(data[1])
    #             points_for_2nd = int(data[2])
    #             points_for_3rd = int(data[3])
    #             athlete_scores = {}
    #             athlete_scores[athlete_name] = [points_for_1st, points_for_2nd, points_for_3rd]
    #             self.update_event_scores(event_name, athlete_scores)

    def calculate_total_points(self, athlete):
        athlete.total_points = sum(self.calculate_event_points(s[0], s[1]) for s in athlete.scores)

    def calculate_event_points(self, event_name, score):
        event = next((e for e in self.events if e.name == event_name), None)
        if event is not None:
            if score == 1:
                return event.points[0]
            elif score == 2:
                return event.points[1]
            elif score == 3:
                return event.points[2]
        return 0

    def rank_athletes(self):
        ranked_athletes = sorted(self.athletes, key=lambda a: a.total_points, reverse=True)
        for i, athlete in enumerate(ranked_athletes):
            athlete.rank = i + 1

    def search_athlete(self, query):
        try:
            rank = int(query)
            athlete = next((a for a in self.athletes if a.rank == rank), None)
        except ValueError:
            athlete = next((a for a in self.athletes if a.name.lower() == query.lower()), None)

        if athlete is not None:
            print(f"{athlete.name} is currently ranked #{athlete.rank} with {athlete.total_points} points")
            if athlete.rank == 1:
                print("Congratulations, you're in first place!")
            else:
                points_to_first = self.calculate_points_to_first(athlete)
                print(f"You need {points_to_first} points to reach first place.")
        else:
            print("Athlete not found.")

    def calculate_points_to_first(self, athlete):
        first_place_points = self.athletes[0].total_points
        return first_place_points - athlete.total_points
    
    def save_data(self):
        with open('data.txt', 'a') as f:
            for event in self.events:
                f.write(event.name + ',' + str(event.points[0]) + ',' + str(event.points[1]) + ',' + str(event.points[2]) + '\n')

    def save_athlete_data(self):
        with open('athlete.txt', 'a') as f:
            for athlete in self.athletes:
                f.write(athlete.name + ',' + str(athlete.total_points) + ',' + str(athlete.rank) + '\n')
                for score in athlete.scores:
                    f.write(score[0] + ',' + str(score[1]) + '\n')