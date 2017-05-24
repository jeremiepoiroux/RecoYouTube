# python 3
# utf-8

import threading
import requests
import csv
import time

from time import ctime
from splinter import Browser
from lxml import html


# ask for start URL
source_url = input('youtube video url to begin the analysis: ')

# ask for csv file title
csv_title = input('csv file title: ')

# header and user-agent
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    }
)

# open browser 
browser = Browser()

# Insert video URL
browser.visit(source_url)

# playlist
playlist = 0

# random value for new_url
new_url = 2

# non-stop loop
# ctrl+c to stop manually


def looper():
    threading.Timer(60, looper).start()

    # requests
    url = browser.url
    r = requests.get(url, headers=headers)

    # tree
    tree = html.fromstring(r.text)

    # video data

    # title cleaning
    title = str(browser.title)
    title = title.rstrip('YouTube')
    # title = title.split(' - ')

    # artist
    # artist = title[0]

    # song
    # song = title[1]

    # views
    views = str(tree.xpath('//div[@class="watch-view-count"]/text()'))
    views = views.lstrip('[\'')
    views = views.rstrip('Anrufe\']')  # Anrufe stands for a german user-agent

    # url
    url = str(browser.url)

    # song code
    code = url.split('=')
    code = code[1]

    # output to csv only if new song
    global new_url
    if new_url != url:
        time.sleep(5)
        # incrementation
        global playlist
        playlist += 1

        # export data in csv
        c = csv.writer(open(csv_title + ".csv", "a"))
        c.writerow((playlist, title, views, url, code, ctime()))

        # print test
        print(str(playlist) + ": " + title)

    else:
        return

    # new_url refresh
    new_url = url

looper()
