import classes

ranking = classes.Ranking()

while True:
    user_type = input("Are you an event organiser or an athlete? ")
    if user_type.lower() == "event organiser":
        event_name = input("Enter the name of the event: ")
        points_for_1st = int(input("Enter the points for 1st place: "))
        points_for_2nd = int(input("Enter the points for 2nd place: "))
        points_for_3rd = int(input("Enter the points for 3rd place: "))
        ranking.add_event(event_name, points_for_1st, points_for_2nd, points_for_3rd)
    elif user_type.lower() == "athlete":
        athlete_name = input("Enter your name: ")
        event_name = input("Enter the name of the event: ")
        score = int(input("Enter your score (1, 2 or 3)s: "))
        ranking.update_athlete_scores(athlete_name, event_name, score)
    else:
        print("Invalid user type. Please try again.")

    query = input("Enter a name or rank to search for an athlete, or 'quit' to exit: ")
    if query.lower() == "quit":
        break
    else:
        ranking.search_athlete(query)