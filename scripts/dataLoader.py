from extractData import read_json_file

DATA_1619 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2016-2019_0.json')
DATA_1922 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2019-2022_1.json')
DATA_2223 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2022-2023_2.json')
DATA_23 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2023_3.json')
DATA_2324 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2023-2024_4.json')
DATA_24 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2024_5.json')
DATA_2425 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2024-2025_6.json')
DATA25 = read_json_file('../data/spotifyStreamData/Streaming_History_Audio_2025_7.json')

FULL_DATA = DATA_1619 + DATA_1922 + DATA_2223 + DATA_23 + DATA_2324 + DATA_24 + DATA_2425 + DATA25