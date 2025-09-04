from dataLoader import FULL_DATA
from extractData import get_Track_Name, calc_track_duration
from convertTime import calc_ms_in_hours, calc_hours_in_days
from processData import filter_10_most_played_for_month

get_Track_Name(FULL_DATA)

def print_duration():
    track_duration = calc_track_duration(FULL_DATA)
    print(f"Total Track Duration: {track_duration} ms")
    track_duration_hours = round(calc_ms_in_hours(track_duration))
    print(f"Total Track Duration: {track_duration_hours} hours")

    track_duration_days = round(calc_hours_in_days(track_duration_hours))
    print(f"Total Track Duration: {track_duration_days} days")

def most_played_songs():
    filter_10_most_played_for_month(2, 2019)

most_played_songs()