import urllib2
from bs4 import BeautifulSoup


data = {}


def scrap_once():
    url = "http://www.rvs.ro/"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    music_div = soup.find("div", {"id": "melodii"})
    songs = music_div.find("ul", {"class": "songs"}).findAll("li")

    new = 0
    for song in songs:
        song_title = song.text.strip()
        if data.get(song_title, None) is None:
            new += 1
        song_url = song.findAll()[0].attrs['data-url']
        data[song_title] = song_url

    return new


def main():
    consecutive_new = 0
    while consecutive_new != 30:
        new = 1
        while new != 0:
            new = scrap_once()
            print "(Re)try: Found {0} new songs. ".format(new)

        if new == 0:
            consecutive_new += 1
        else:
            consecutive_new = 0

    print "Total songs found: {0}".format(len(data.keys()))

    print "The list of URLs:"
    for song_title in data.keys():
        song_url = data[song_title]
        print "{0}".format(song_url)
