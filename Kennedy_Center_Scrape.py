# --------------------------------------------------- #
#
# Events Scraper: gets the upcoming events from the
# Kennedy Center website, then updates csv file with
# latest events as an array of dictionaries.
# Bri's Version
#
# --------------------------------------------------- #

from urllib.request import urlopen, request
from bs4 import BeautifulSoup
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "http://www.kennedy-center.org/calendar/"
my_url = base_url + "upcoming"

# while in the events sections, grab:
# Title
# Description of the event
# links of events
# Datetime(s) of event
# Image url of the event
# Reservation link

#create a user-agent in the form of a dictionary
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "From": "youremail@domain.com"  # This is another valid field
}

response = request.get(base_url, headers=headers)

# opening up connection, grabbing the page
webpage = urlopen(response).read()

#artificial click times
#sleep for a second

# closes connection
webpage.close()

# html parsing
soup = BeautifulSoup(webpage, "html.parser")

# get the main table results
results = soup.findAll("div", attrs={"class":"event-tile"})
print(results)

#record event info
events = []

# Create loop to grab event info
#for info in results:



    #stores each events's info
#    event = {}

    #grab title
#    title = info.find("img", {"class": "img-responsive"})
#    title_text = (title['alt'])
#    event["title"] = title_text

    #grab description
#    description = info.find("p", attrs={"class": "hidden-xs"})
#    description_text = description.text.strip()
#    event["description"] = description_text

    #grab links
#    link = info.find("div", attrs={"class": "col-sm-8 col-xs-8"})
#    link_text = link.a["href"]
#    website_text = (base_url + link_text)
#    event["website"] = website_text

    #grab date and time
#    date = info.find("small")
#    date_text = date.text.strip()
#    event["datetime"] = date_text

    #grab image url
#    image = info.find("img", attrs = {"class": "img-responsive"})
#    image_text = image["src"]
#    event["image_url"] = image_text

    #appends all events
#    events.append(event)


#Headlines = ["title", "description", "website", "datetime", "image_url"]

#try:
    # Open the csv to import data
#    with open("kennedy_center.csv", "w", newline='', encoding="utf8") as csv_file:
#        writer = csv.DictWriter(csv_file, fieldnames=Headlines)
#        writer.writeheader()
#        for event in events:
#            writer.writerow(event)
#except IOError:
#    print("I/O Error")
