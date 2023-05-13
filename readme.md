# README

This is a Python application that allows event organizers to create events and add athletes with their scores. It also provides a feature to search for athletes based on their names or ranks.

## Installation
Clone the repository or download the files to your local machine.
Make sure Python 3.x is installed on your machine.
Install the following dependencies using pip:
colored

## Dependencies
Python 3.x
colored

## Usage
open run.sh
or
Open a terminal or command prompt and navigate to the directory where the files are saved.
Run the main.py file using the following command:
python main.py

When prompted, select whether you are an event organizer or an athlete.
If you select 'event organizer', enter the name of the event, points for 1st place, 2nd place and 3rd place.
If you select 'athlete', enter your name, the name of the event and your score (1, 2 or 3).
To search for an athlete, enter their name or rank when prompted. You can also type 'quit' to exit the application.
To see a list of current events, enter 'yes' when prompted after the above step.
Note: The data for events and athletes are stored in separate text files named 'data.txt' and 'athlete_data.txt' respectively. These files will be created automatically when the application is run for the first time. If you wish to delete the data, simply delete these files.
