# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib


import re
#import urllib.request as urllib2
from lxml import etree
from lxml import html

#import schedule
import datetime

#import schedule

import selenium
import chromedriver

def job(url, building_name):
    print("I'm working...")

    # while this is true (it is true by default),

    # set the url as VentureBeat,

    #url = "http://ravelresidence.studentexperience.nl/"
    # set the headers like we are a browser,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    page = requests.get(url)
    # tree = html.fromstring(page.content)

    content = page.content

    soup = BeautifulSoup(content, 'html.parser')

    #
    # count = 0
    # for string in soup.stripped_strings:
    #     if string == 'Geen woning(en)':
    #         print(True)
    #         count += 1
    #
    # # if the number of times the word "Google" occurs on the page is less than 1,
    # if count == 4:
    #     # wait 60 seconds,
    #     print("yes")
    #     time.sleep(20)
    #     pass
    #     # continue with the script
    #
    # # but if the word "Google" occurs any other number of times,
    # else:
    #     # create an email message with just a subject line,
    #     msg = 'Subject:' +building_name + "Room Available"
    #     body=""
    #     # set the 'from' address,
    #     fromaddr = 'sjdoyle@gmail.com'
    #     # set the 'to' addresses,
    #     toaddrs = ['sjdoyle46@gmail.com']
    #
    #     # setup the email server,
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     # add my account login name and password,
    #     server.login("sjdoyle46@gmail.com", "Webshannon2")
    #
    #     # Print the email's contents
    #     print('From: ' + fromaddr)
    #     print('To: ' + str(toaddrs))
    #     print('Message: ' + msg)
    #
    #     # send the email
    #     server.sendmail(fromaddr, toaddrs, msg)
    #     # disconnect from the server
    #     server.quit()




run_ravel_script=False
currentDT = datetime.datetime.now()

hour = currentDT.hour
# currentDT.minute
weekday = str(currentDT.strftime("%a"))
if weekday not in ["Sat", "Sun"]:
    print("not weekened")
    weekday = True

if weekday == True:
    if hour in range(9, 13):
        print(hour)
        run_ravel_script = True
    else:
        print("not correct time")

#print(run_ravel_script)


while  run_ravel_script == True:
    print("correct time")
    job("http://ravelresidence.studentexperience.nl/", "Raval")
    job("http://roomselector.studentexperience.nl/index.php" , "Amstel")





