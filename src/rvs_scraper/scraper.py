import urllib2
from bs4 import BeautifulSoup


data = {}


def main():
    url = "http://www.rvs.ro/"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    music_div = soup.find("div", {"id": "melodii"})
    songs = music_div.find("ul", {"class": "songs"}).findAll("li")

    for song in songs:
        song_title = song.text.strip()
        data[song_title] = song_title

    print data
