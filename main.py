import classes
import os

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
        ranking.save_data()  # save event data to the file
        ranking.save_athlete_data() # save athlete data to text file
        break
    else:
        ranking.search_athlete(query)

user_input = input("Do you want to see the list of current events? (yes/no) ")

# Check user input and print events
if user_input.lower() == "yes":
    with open("data.txt", "r") as file:
        events = []
        for line in file:
            data = line.strip().split(",")
            if data[0] not in events:
                events.append(data[0])
        print("Current Events:")
        for event in events:
            print("- " + event)