import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_Track_Name(data):
    with open('../output/output.txt', 'w') as f:
        for i, track in enumerate(data, start=1):
            f.write(f"Track {i}:\n")
            f.write(f"Track Name: {track['master_metadata_track_name']}\n")
            f.write(f"Album Artist: {track['master_metadata_album_artist_name']}\n")

def calc_track_duration(data):
    total_duration = sum(track['ms_played'] for track in data)
    return total_duration
