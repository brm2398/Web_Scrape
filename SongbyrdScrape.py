# --------------------------------------------------- #
#
# Events Scraper: gets the upcoming events from the
# Songbyrd website, then updates csv file with
# latest events as an array of dictionaries.
# Bri's Version
#
# --------------------------------------------------- #

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://www.songbyrddc.com/"
my_url = "https://www.songbyrddc.com/music-venue/"


# while in the events sections, grab:
# Title
# Description of the event
# links of events
# Datetime(s) of event
# Image url of the event
# Reservation link

# opening up connection, grabbing the page
uClient = uReq(my_url)
#offloads connection content into a variable
page_html = uClient.read()
# closes connection
uClient.close()

# html parsing
soup = BeautifulSoup(page_html, "html.parser")

# get the main table results
results = soup.findAll("div", attrs={"class":"row event-item"})

#record event info
events = []

# Create loop to grab event info
for info in results:

    #stores each events's info
    event = {}

    #grab title
    title = info.find("a", {"class":"event-link"})
    title_text = title.text.strip()
    event["title"] = title_text
    #Next challenge would be to change titles to sentence case

    #grab description
    description = info.find("div", attrs={"class": "col-xs-12 col-md-5"})
    description_text = description.text.strip()
    event["description"] = description_text

    #grab links
    link = info.find("div", attrs={"class": "col-xs-12 col-md-5"})
    link_text = link.a["href"]
    website_text = (base_url + link_text)
    event["website"] = website_text

    #grab date
    date = info.find("span", attrs={"class":"eventDate"})
    date_text = date["v"]
    event["datetime"] = date_text

    #grab image url
    image = info.find("img")
    image_text = base_url + image["src"]
    event["image_url"] = image_text
    print(event)

    #appends all events
    events.append(event)


Headlines = ["title", "description", "website", "datetime", "image_url"]

try:
    # Open the csv to import data
    with open("Songbyrd_Scrape.csv", "w", newline='', encoding="utf8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=Headlines)
        writer.writeheader()
        for event in events:
            writer.writerow(event)
except IOError:
    print("I/O Error")

