from datetime import datetime
from dataLoader import FULL_DATA

def filter_tracks_for_month(data, month, year):
    return [
        item for item in data
        if datetime.strptime(item["ts"], "%Y-%m-%dT%H:%M:%SZ").month == month
        and datetime.strptime(item["ts"], "%Y-%m-%dT%H:%M:%SZ").year == year
    ]

def filter_10_most_played_for_month(month, year):
    dataJanuary = filter_tracks_for_month(FULL_DATA, month, year)
    sortedDataJanuary = sorted(dataJanuary, key=lambda x: x['ms_played'], reverse=True)

    with open('../output/test.txt', 'w') as f:
        for i, item in enumerate(sortedDataJanuary[:10], start=1):
            track_name = item.get("master_metadata_track_name") or item.get("episode_name")
            ms_played = item.get("ms_played", 0)
            f.write(f"{i}. {track_name} - {ms_played} ms\n")