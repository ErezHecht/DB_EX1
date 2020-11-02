import csv
from io import TextIOWrapper
from zipfile import ZipFile

MAX_LINES = 10000

# opens file for olympics table.
# CHANGE!
outfile = open("olympics.csv", 'w', )
outwriter = csv.writer(outfile, delimiter=",", quoting=csv.QUOTE_NONE)

athlete_file = open("athlete.csv", 'w', )
event_file = open("event.csv", 'w', )
games_file = open("games.csv", 'w', )
team_file = open("team.csv", 'w', )
participation_file = open("participation.csv", 'w', )

athletewriter = csv.writer(athlete_file, delimiter=",", quoting=csv.QUOTE_NONE)
eventwriter = csv.writer(event_file, delimiter=",", quoting=csv.QUOTE_NONE)
gameswriter = csv.writer(games_file, delimiter=",", quoting=csv.QUOTE_NONE)
teamwriter = csv.writer(team_file, delimiter=",", quoting=csv.QUOTE_NONE)
participationwriter = csv.writer(participation_file, delimiter=",", quoting=csv.QUOTE_NONE)


# process_file goes over all rows in original csv file, and sends each row to process_row()
# DO NOT CHANGE!!!
def process_file():
    counter = 0
    with ZipFile('athlete_events.csv.zip') as zf:
        with zf.open('athlete_events.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                # pre-process : remove all quotation marks from input and turns NA into null value ''.
                row = [v.replace(',', '') for v in row]
                row = [v.replace("'", '') for v in row]
                row = [v.replace('"', '') for v in row]
                row = [v if v != 'NA' else "" for v in row]
                # in 'Sailing', the medal winning rules are different than the rest of olympic games, so they are discarded.
                if sport == "Sailing":
                    continue
                process_row(row)
                counter += 1
                if counter == MAX_LINES:
                    break


# process_row should splits row into the different csv table files
# CHANGE!!!
def process_row(row):
    outwriter.writerow(row)


# return the list of all tables
# CHANGE!!!
def get_names():
    return ["athlete", "team", "event", "games", "participation"]


if __name__ == "__main__":
    process_file()
