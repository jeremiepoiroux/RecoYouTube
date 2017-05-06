# python 3
# utf-8

import threading
import requests
import sys
import csv

from splinter import Browser
from lxml import html

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
browser.visit('https://www.youtube.com/watch?v=YQHsXMglC9A')

# non-stop loop
# ctrl+c to stop manually
def looper():    
    # i as interval in seconds    
    threading.Timer(5, looper).start()   

    # requests
    url  = browser.url
    r = requests.get(url, headers=headers)

    # tree
    tree = html.fromstring(r.text)

    # video data

    ## title cleaning
    title = str(browser.title)
    title = title.strip('YouTube')
    title = title.split(' - ')

    ## artist
    artist = title[0]

    ## song
    song = title[1]

    ## views
    views = str(tree.xpath('//div[@class="watch-view-count"]/text()'))
    views = views.lstrip('[\'')
    views = views.rstrip('Anrufe\']') 

    ## url
    url = str(browser.url)

    ## song code
    code = url.split('=')
    code = code[1]

    # export data in csv
    c = csv.writer(open("adele4.csv", "a"))
    c.writerow((artist,song,views,url,code))

#    currentartist = print(artist)
#
#    if currentartist == artist:
#    	print("identique")

#    else:
#    	print("different")

#to start 
looper()