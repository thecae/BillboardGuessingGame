import random
import requests
from bs4 import BeautifulSoup


def read_data(num_songs):
    ALL_TRACKS = []

    url = 'https://www.billboard.com/charts/hot-100'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    spans = soup.find_all('span', {'class': 'chart-element__information'})
    print(spans)

    if len(spans) > 0:
        for s in range(len(spans)):
            track = [str(s + 1), spans[s].find('span', {'class': 'chart-element__information__song'}).text,
                     spans[s].find('span', {'class': 'chart-element__information__artist'}).text]
            ALL_TRACKS.append(track)
    random_numbers = random.sample(range(0, 99), num_songs)
    random_songs = []
    for number in random_numbers:
        random_songs.append(ALL_TRACKS[number])
    return random_songs


def order_songs(songs, num_songs):
    song_order = [int(song[0]) for song in songs]
    ordered_songs = sorted(song_order)
    string_order = ''
    for x in range(num_songs): string_order += str(song_order.index(ordered_songs[x]) + 1)
    return string_order


def reorder_songs(songs, num_songs):
    order = order_songs(songs, num_songs)
    index = ''
    ordered_songs = []
    for x in range(num_songs): index += str(order.index(str(x + 1)))
    for x in range(len(index)): ordered_songs.append(songs[index.index(str(x))])
    return ordered_songs


def print_songs_numbered(songs, song_num):
    return ' ' + songs[song_num][0] + ': ' + songs[song_num][1] + ' - ' + songs[song_num][2]


def print_songs(songs, song_num):
    return songs[song_num][1] + ' - ' + songs[song_num][2]


num_songs = 3  # if time permits, work on changing everything to allow for any number
songs = read_data(num_songs)
song_guess = ''
song_order = order_songs(songs, num_songs)
