# --------------------------------------------------- #
#
# Events Scraper: gets the upcoming events from the
# Millenium Stage website, then updates csv file with
# latest polls.
# Bri's Version
#
# --------------------------------------------------- #

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
import csv
from datetime import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import schedule
from urllib.request import urlopen
import re

ssl._create_default_https_context = ssl._create_unverified_context

my_url = "https://www.kennedy-center.org/video/upcoming"

# opening up connection, grabbing the page

uClient = uReq(my_url)

# offloads connection content into a variable

page_html = uClient.read()

# closes connection

uClient.close()

# holds the events of the polls currently in the csv
data = []

# html parsing

page_soup = soup(page_html, "html.parser")

# get titles and img url

titles = page_soup.findAll("div", {"class": "col-sm-4 col-xs-4"})
# descriptions = page_soup.find("p", {"class": "hidden-xs"})
image_divs = page_soup.findAll("div", {"class": "col-sm-4 col-xs-4"})

# grabs the event title that is nested in a div
for tit in titles:
    for t in tit.findAll("img", {"class": "img-responsive"}):
        title_text = (t['alt'])
        f = title_text

# grabs the event image urls that are nested in a div
for div in image_divs:
    for img in div.findAll("img", {"class": "img-responsive"}):
        image_url = (img['src'])
        g = image_url

    data.append((f, g))

# open the csv file and import data into csv

with open("mill_scrape_Bri.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    # The for loop
    for f, g in data:
        writer.writerow([f,g ])








