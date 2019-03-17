import urllib2
from bs4 import BeautifulSoup


def main():
    url = "http://www.rvs.ro/"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    music_div = soup.find("div", {"id": "melodii"})
    import pdb; pdb.set_trace()
