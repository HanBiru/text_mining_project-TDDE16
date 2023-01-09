import time
import lyricsgenius #https://github.com/johnwmillr/LyricsGenius/tree/master/lyricsgenius

# Replace YOUR_ACCESS_TOKEN with your actual Genius API access token
TOKEN = 'YOUR_ACCESS_TOKEN'
genius = lyricsgenius.Genius(TOKEN)

# Added some testsongs
song_list = [
    ('Let it be', 'The Beatles'),
    ('Lemon', 'Yonezu Kenshi'),
    ('Yellow', 'cold play')
    # Add more songs to the list as needed
]

# Set the rate limit for the Genius API (1,000 requests per hour for non-authenticated users)
rate_limit = 1000

# Set the time between requests to the Genius API (in seconds)
request_delay = 3600 / rate_limit

for song_title, artist_name in song_list:
    
    song = genius.search_song(title =song_title, artist = artist_name)
    print(song.lyrics)


    # Wait the specified amount of time before making the next request
    time.sleep(request_delay)
