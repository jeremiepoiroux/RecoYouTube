#!/usr/bin/env python3
# coding: utf-8

import requests
import sys
from lxml import html

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    }
)

url = "https://www.youtube.com/watch?v=hLQl3WQQoQ0"

r = requests.get(url, headers=headers)
if r.status_code != 200:
    print("couille dans le bouillon")
    print(url)
    sys.exit()

tree = html.fromstring(r.text)

title = tree.xpath('//span[@class="watch-title"]/text()')
views = tree.xpath('//div[@class="watch-view-count"]/text()')
nextvideo = tree.xpath('//span[@class="title"]/text()')
nextvideoviews = tree.xpath('//span[@class="stat view-count"]/text()')
# nextvideourl = tree.xpath('//*[@id="watch7-sidebar-modules"]/div[1]/div/div[2]/ul/li/div[1]/a/href//text()')


print(title)
print(views)
print(nextvideo[0])
print(nextvideoviews[0])
# print(nextvideourl)


