import classes
import os
from colored import fg, bg, attr

ranking = classes.Ranking()

while True:
    user_type = input(f"{fg(234)}{bg(136)}Are you an event organiser or an athlete? {attr(0)}")
    if user_type.lower() == "event organiser":
        event_name = input(f"{fg(94)}{bg(0)}Enter the name of the event: {attr(0)}")
        while True:
            try:
                points_for_1st = int(input(f"{fg(142)}{bg(0)}Enter the points for 1st place: {attr(0)}"))
                points_for_2nd = int(input(f"{fg(231)}{bg(0)}Enter the points for 2nd place: {attr(0)}"))
                points_for_3rd = int(input(f"{fg(94)}{bg(0)}Enter the points for 3rd place: {attr(0)}"))
                break  # exit the loop if valid input is entered
            except (ValueError, KeyError, NameError):
                print("Please enter a valid number")
        ranking.add_event(event_name, points_for_1st, points_for_2nd, points_for_3rd)
    elif user_type.lower() == "athlete":
        athlete_name = input("Enter your name: ")
        event_name = input("Enter the name of the event: ")
        score = int(input("Enter your score (1, 2 or 3)s: "))
        ranking.update_athlete_scores(athlete_name, event_name, score)
    else:
        print("Invalid user type. Please try again.")

    query = input("Enter a name or rank to search for an athlete, 'quit' to exit or press 'enter' to add new event or athlete: ")
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