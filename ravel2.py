# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:33:41 2019

@author: doyle
"""


import datetime
run_ravel_script=False


#start_time = time.time()
currentDT = datetime.datetime.now()

hour=currentDT.hour
#currentDT.minute
weekday= str(currentDT.strftime("%a"))
if weekday not in ["Sat", "Sun"]:
    print("not weekened")
    weekday=True



if weekday==True:
    if hour in range(10, 14):
        print(hour)
        run_ravel_script=True

print(run_ravel_script)
        
if run_ravel_script==True: 
    print(True)
    job()
    
        







#%%
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


#%%


def job():
    print("I'm working...")


    # while this is true (it is true by default),

        # set the url as VentureBeat,
       
    url="http://ravelresidence.studentexperience.nl/"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    page = requests.get(url)
    #tree = html.fromstring(page.content)

    content=page.content

    soup = BeautifulSoup(content, 'html.parser')

    count=0
    for string in soup.stripped_strings:
        if string=='Geen woning(en)':
            print(True)
            count+=1


    # if the number of times the word "Google" occurs on the page is less than 1,
    if count == 5:
        # wait 60 seconds,
        print("yes")
        time.sleep(60)
        pass
        # continue with the script

    # but if the word "Google" occurs any other number of times,
    else:
        # create an email message with just a subject line,
        msg = 'Subject: Raval room!'
        # set the 'from' address,
        fromaddr = 'sjdoyle@gmail.com'
        # set the 'to' addresses,
        toaddrs  = ['sjdoyle46@gmail.com']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("sjdoyle46@gmail.com", "Webshannon2")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()
        
        

#%%
        


hour=currentDT.hour
#currentDT.minute
weekday= str(currentDT.strftime("%a"))
if weekday not in ["Sat", "Sun"]:
    print("not weekened")
    weekday==True

run_raval_script=False
if weekday==True:
    if hour=="10" or "11":
        run_raval_script=True
        



    



#job()
#schedule.every().day.at("01:54").do(job())
schedule.every(1).minutes.do(job())
#schedule.run_pending()


# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)



while run_raval_script==True:
    schedule.run_pending()
    #time.sleep(1)



#%%
 
