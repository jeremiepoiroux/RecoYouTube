# python 3
# utf-8

import threading
import requests
import sys

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

# go to Adele - Hello video on Youtube
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

    # data current video
    title = str(browser.title)
    url = str(browser.url)
    views = str(tree.xpath('//div[@class="watch-view-count"]/text()'))

    # data next video
    titlenext = str(tree.xpath('//span[@class="title"]/text()'))
    viewsnexr = str(tree.xpath('//span[@class="stat view-count"]/text()'))
    # nextvideourl = tree.xpath('//*[@id="watch7-sidebar-modules"]/div[1]/div/div[2]/ul/li/div[1]/a/href//text()')

    # export data in file
    file = open("adele.txt", "a")
    file.write(title + " ")
    file.write(url + " ")
    file.write(views + " ")
    file.write("\n")
    file.close()

    # print check
    print ("ok")

#to start 
looper()